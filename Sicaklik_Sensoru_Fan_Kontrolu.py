import RPi.GPIO as GPIO
import os
import glob
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.cleanup()
K_led = 5
Y_led = 10
buzzer  = 26
motorileri = 18
motorgeri = 16
motordur = 22

GPIO.setup(K_led,GPIO.OUT)
GPIO.setup(Y_led,GPIO.OUT)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.setup(motorileri,GPIO.OUT)
GPIO.setup(motorgeri,GPIO.OUT)
GPIO.setup(motordur,GPIO.OUT)
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'                   # Kütüphane içerisindeki dosyaya bu komut ile  erişiyoruz
device_folder = glob.glob(base_dir + '28*')[0]      # base_dir içindeki 28 ile biten tüm dosyaları al
device_file = device_folder + '/w1_slave'           # dosya isimlerinin sonun w1_slave  ekle


def read_temp_raw():
    f = open(device_file, 'r')                  # az önce değişiklik yapılan dosyaları okuma modunda
    lines = f.readlines()
    f.close()
    return lines


def motorsarti(temperature):

    if temperature >= 40:
        GPIO.output(motorileri,GPIO.HIGH)
        GPIO.output(motorgeri,GPIO.LOW)
        GPIO.output(motordur,GPIO.HIGH)
        
    elif temperature < 40:
        GPIO.output(motorileri,GPIO.LOW)
        GPIO.output(motorgeri,GPIO.HIGH)
        GPIO.output(motordur,GPIO.HIGH)
        print ("Ortam sıcaklığı ideal")

 
def read_temp():
    
    lines = read_temp_raw()                     
    while lines[0].strip()[-3:] != 'YES':               # Wire kütüphanesinin protokollerinin açık-
        time.sleep(0.2)                                 # olup olmadığını kontrol eder (veri varmı  yokmu)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f


def TriggerLightAndBuzzer(temperature):

    if temperature >= 40 and temperature < 70:
        GPIO.output(buzzer,0)       # Buzzer On
        GPIO.output(Y_led, 0)       # Yeşil led Off
        GPIO.output(K_led,1)        # Kırmızı led On
    elif temperature < 40: 
        GPIO.output(buzzer, 0)      # Buzzer Off
        GPIO.output(Y_led,1)        # Yeşil led On
        GPIO.output(K_led, 0)       # Kırmızı led Off
    elif temperature >= 70:
        GPIO.output(buzzer, 1)      # Buzzer On
        GPIO.output(Y_led, 0)       # Yeşil led Off
        GPIO.output(K_led,1)        # Kırmızı led On        
        print("Sıcaklık acilen düşmeli !")
                
    print(temperature)      # Mevcut sıcaklık


while True:
    currentTempAsCelcius, currentTempAsFahrenait = read_temp()
    TriggerLightAndBuzzer(currentTempAsCelcius)
    motorsarti(currentTempAsCelcius)
    time.sleep(2)
    
    


