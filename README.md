# Sicaklik_Sensoru_DC_Fan

Raspberyy GPIO pinlerinin hepsini kullanabilmek için aşağıdaki adımları uygulayınız; <br>
Raspberyy Pi konsolunu açınız. <br>
𝙨𝙪𝙙𝙤 𝙖𝙥𝙩-𝙜𝙚𝙩 𝙪𝙥𝙙𝙖𝙩𝙚 <br>
𝙨𝙪𝙙𝙤 𝙖𝙥𝙩-𝙜𝙚𝙩 𝙞𝙣𝙨𝙩𝙖𝙡𝙡 𝙥𝙮𝙩𝙝𝙤𝙣-𝙙𝙚𝙫 <br>
komutlarını yazarak yüklemeleri yapınız. (Rasperry PI gerekli güncellemeler) <br>

𝙂𝙋𝙄𝙊 𝙆𝙪̈𝙩𝙪̈𝙥𝙝𝙖𝙣𝙚𝙨𝙞𝙣𝙞𝙣 𝘾̧𝙖𝙜̆ı𝙧ı𝙡𝙢𝙖𝙨ı :  <br>
Raspberry Pi kartınızda GPIO kütüphanesinin ismi RPi.GPIO olarak kullanılmaktadır. Python programında bu kütüphaneyi eklemek için aşağıdaki komut kullanılmaktadır.
>> import RPi.GPIO

GPIO kütüphanesini programda daha sonra GPIO ismiyle çağırmak için aşağıdaki kod kullanılmaktadır.

>> import RPi.GPIO as GPIO

𝙂𝙋𝙄𝙊 𝙋𝙞𝙣 𝙏𝙪̈𝙧𝙪̈𝙣𝙪̈𝙣 𝘼𝙮𝙖𝙧𝙡𝙖𝙣𝙢𝙖𝙨ı : <br> 
Raspberry Pi’ın GPIO pinlerini isimlendirirken iki farklıdizilimle karşılaşırız. Bunlar BCM dizilimi ve BOARD dizilimidir. BCM dizilimi pinlere verilen GPIO numaralarından oluşmaktadır. Bunlar sıralı numaralar değildir. BOARD dizilimi ise pinlerin fiziksel numaralandırılmasıdır. 1’den başlayıp 40’a kadar devam eden sıralı sayılardan oluşur.
Resimde Raspberry Pi'nin pin girişleri ve isimleri yer almaktadır. <br>

![gpio-pinout-diagram](https://user-images.githubusercontent.com/106193850/187070778-c4f0181f-84a5-4524-9053-1717bb102509.png) <br>
 
 **Sıcaklık Sensörü:** <br>
 
DS18B20 Dijital Sıcaklık Sensörü 12 bitlik hassas bir ölçüm aralığında 1-tel olarak kullanılabilen bir sıcaklık sensörüdür. DS18B20 sensörleri tek tel destekleyen mikroişlemcilerle iletişim kurabilme özelliğine sahiptir. Bir pinde birden fazla sensör aynı anda kullanılabilir. Her sensörün kendine özgü 64 bitlik bir seri numarası vardır. Bu sebeple tüm sensörler birbirinden ayırt edilebilir. Enerji girişi olarak 3.3V ya da 5V tercih edilebilir. <br>

**Kullanılacak Malzemeler** <br>

•	Bread Board <br>
•	DS18B20 Sıcaklık Sensörü <br>
•	Raspberry Pi <br>
•	Jumper kablo(d-e, e-e) <br>
•	Direnç (4.7 Kohm) <br>
• DC motorla çalışan fan <br>
• L293D Motor Sürücü Entegresi <br>
•	Direnç (4.7 Kohm) <br>

Sıcaklık sensörünün raspberry'e bağlantı şekli aşağıdaki şekilde gösterilmiştir.<br>

![seıcaklık sensöür](https://user-images.githubusercontent.com/106193850/187076859-20b4c9b9-1285-459b-9bca-f28c2c4cc286.png) <br>

Yukarıdaki devre bağlantılarını gerçekleştirdikten sonra aşağıdaki kodlar ile 1-Wire haberleşme protokolünü açıyoruz. ( Raspberry Pi Cihazına HDMI kablo ile bağlanmanız önerilir ) <br>

Config dosyasına erişim sağlamak için : <br>

>>  sudo nano /boot/config.txt      

![image](https://user-images.githubusercontent.com/106193850/187077138-ca0ac946-ba1a-400c-9f2c-89d2a8b81b3f.png) <br>

config.txt dosyası olmak zorundadır. <br>

**L293D Motor Sürücü Entegresi**  <br>

L293D Motor Sürücü entegresi DIP-16 kılıftadır. 4.5 V - 36 V arasında giriş gerilimine sahip olan bu Motor Sürücü entegresi 39 V'a kadar çıkış gerilimi sunmaktadır. Toplamda 4 adet çıkışa sahip olan bu Motor Sürücü entegresi bu çıkışlardan 1.2A 'e kadar akım verebilmektedir. Bu Motor Sürücü entegresi Half H Bridge sürücü konfigürasyonunu kullanmaktadır. <br>

![devre](https://user-images.githubusercontent.com/106193850/187081130-8638e29a-f253-4e0a-b5c7-ccbe6eaca6ac.jpg)  <br>

**Pin Bağlantıları:** <br>
•	4-5-12-13 nolu bacaklar birleştirilip toprak hattına bağlanmalıdır. <br>
•	Motorlar, 3-6 ve 11-14 nolu bacaklara bağlanır. <br>
•	1-16-9 nolu bacaklara volt verilir. <br>
•	2 ve 7 nolu bacaklar 1. Motorun, 10 ve 15 nolu bacaklar 2. motorun yönünü belirler. <br>
•	8 nolu bacaktan, motora uygulanacak voltaj verilir. <br>

**Uygulama Yapılışı ve Çalışması:** <br>
<p> Bread Board üzerine devre kurulur. Pin ve diğer bağlantılar yukarıdaki şemalarda belirtildiği gibi bağlantılar yapılır. Raspberrynin pin bağlnatıları da gerçekleştirilip python kodlarımız raspberry üzerinden çalıştırılır. <br>

<p> Projede sıcaklık güncel sıcaklığı sürekli ölçerek ekrana yazdırmaktadır. Sıcaklık 40°C'nin altında iken, yeşil led yanar ve ekrana 'Ortam Sıcaklığı İdeal' diye yazı yazdırır ve DC motor ile çalışan fan geri yönde dönmeye başlar. Sıcaklık 40°C ve 70°C arasına gelince, yeşil led söner bu sefer kırmızı led yanmaya başlar. Sıcaklık 40°C'nin üstüne çıktıktan sonra fan geri dönme hareketini sonlandırıp ileri yönde dönme hareketine başlar. Sıcaklık 70°C'nin üzerine çıkınca ise kırmızı led yanar ve buzzer çalışır, ekrana ise 'Sıcaklık acilen düşmeli !' şeklinde bir uyarı gelir. Bu işlemler sırasında ekrana güncel sıcaklık bilgisi sürekli gelmektedir. <br>

Proje ile ilgili kodlara, kodlar kısmından ulaşabilirsiniz.










 
