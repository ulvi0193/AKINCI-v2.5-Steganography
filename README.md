<img width="2752" height="1536" alt="da4244c30024f12288644aef" src="https://github.com/user-attachments/assets/e3824049-f70a-4eec-b9f4-bb1c85aa44c6" />
# 🦅 AKINCI v2.5 - Kriptografik Steganografi Muhafızı

AKINCI, siber güvenlik operasyonlarında, sızma testlerinde (Red Team / CTF) ve güvenli veri paylaşımlarında gizliliği en üst düzeye çıkarmak için geliştirilmiş, Python tabanlı bir **EOF (End-of-File) Steganografi** aracıdır. 

Harici hiçbir üçüncü parti Python kütüphanesine (`Pillow`, `OpenCV` vb.) ihtiyaç duymadan, tamamen standart yerel modüllerle ve optimize edilmiş modern bir grafik arayüzle (GUI) çalışır.

---

## ⚡ Temel Özellikler & Güvenlik Mimarisi

* **Çift Katmanlı Koruma:** Gizlenen veriler önce **XOR** algoritması ile karakter bazlı şifrelenir, ardından veri taşınabilirliği için **Base64** formatına kodlanarak dosya sonuna (EOF) enjekte edilir.
* **Hex Editör Kalkanı:** Gömülen veriler ham metin olarak değil, kriptografik çorba veri olarak saklandığı için Hex editörlerle bakıldığında doğrudan okunamaz.
* **Sıfır Bağımlılık (Zero-Dependency):** Sadece `tkinter`, `base64` ve `os` gibi yerel kütüphaneleri kullanır. Kurulum derdi olmadan her sistemde doğrudan çalıştırılabilir.
* **ANSI Banner Girişi:** Terminal üzerinden başlatıldığında göz alıcı bir siber operasyon banner'ı ile saniyeler içinde arayüze geçiş yapar.

---

## 🚀 v2.5 İle Gelen Siber Yenilikler

Eski sürümlerdeki kararsızlıklar ve kısıtlamalar bu sürümde tamamen giderilerek araç kurumsal test standartlarına uygun hale getirilmiştir:

### 🛡️ 1. Orijinal Uzantı Kalkanı
* **Eski Sorun:** `.jpg` veya `.jpeg` dosyaları seçildiğinde sistem çıktıyı zorla `.png` yapıyordu ve bu durum dosya imzasını (Magic Bytes) bozabiliyordu.
* **v2.5 Çözümü:** `os.path.splitext` mekanizması entegre edildi. Kaynak resmin orijinal uzantısı havada yakalanır ve sistem dosya bütünlüğünü korumak adına o formatı bozmadan kaydetmeye zorlanır.

### 📊 2. Çok Satırlı Siber Rapor Desteği (`ScrolledText`)
* **Eski Sorun:** Tek satırlık dar `Entry` kutuları uzun mesajlarda veya loglarda yetersiz kalıyordu.
* **v2.5 Çözümü:** Dar kutular tamamen söküldü! Yerine hem mesaj gizlerken hem de deşifre ederken koca siber istihbarat raporlarını, geniş log çıktılarını veya uzun URL adreslerini rahatça alabilecek kaydırılabilir hacker pencereleri eklendi.

### 🛡️ 3. Sızdırmaz Hata Denetimi (Crash-Proof)
* **Eski Sorun:** İçinde veri olmayan temiz bir resim analiz edilmek istendiğinde veya işlem yarıda kaldığında program çöküyordu.
* **v2.5 Çözümü:** Tüm kritik fonksiyonlar `try-except` kalkanları ile sarıldı. Artık analiz edilen temiz dosyalarda program donmaz veya çökmez; akıllıca `Temiz Dosya // AKINCI Yapısı Bulunamadı` uyarısı vererek kararlı çalışmasını sürdürür.

### 🔑 4. Çoklu Marker Çakışması Engellendi
* **Eski Sorun:** Resmin byte dizilimi taranırken imza çakışmaları yaşanabiliyordu.
* **v2.5 Çözümü:** Ayraç imza (`##AKINCI_v2##`) tarama mantığı ve `split` bölme motoru daha kararlı hale getirildi. İki imzanın tam ortasında kalan şifreli base64 verisi adeta cımbızla çekilerek hatasız deşifre edilir.

---

## 🛠️ Kurulum ve Çalıştırma

Herhangi bir kütüphane yüklemenize gerek yoktur. Bilgisayarınızda Python 3'ün kurulu olması yeterlidir.

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/ulvi0193/AKINCI-Steganography
   cd AKINCI-Steganography
   python akinci25.py
```
