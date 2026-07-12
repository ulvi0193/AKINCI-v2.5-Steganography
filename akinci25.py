import os

import sys

import time

import base64

import tkinter as tk

from tkinter import scrolledtext

from tkinter import ttk, messagebox, filedialog



# ==========================================

# 1. KRİPTOGRAFİ VE ARKA PLAN MANTIĞI (v2.5)

# ==========================================



# Verileri Hex editörlerden gizlemek için kullanacağımız benzersiz anahtar

GIZLI_ANAHTAR = "Exorcıst"

START_MARKER = b"##AKINCI_v2##"



def xor_sifrele_coz(veri: str, anahtar: str) -> str:

    """Veriyi karakter bazlı XOR işlemine sokarak şifreler veya çözer."""

    return "".join(chr(ord(c) ^ ord(anahtar[i % len(anahtar)])) for i, c in enumerate(veri))



def metni_kriptola(mesaj: str) -> bytes:

    """Düz metni önce XOR ile şifreler, ardından taşınabilir olması için Base64'e çevirir."""

    sifreli_metin = xor_sifrele_coz(mesaj, GIZLI_ANAHTAR)

    b64_byte = base64.b64encode(sifreli_metin.encode('utf-8'))

    return b64_byte



def kriptolu_metni_coz(b64_byte: bytes) -> str:

    """Base64 formatındaki şifreli veriyi çözer ve XOR anahtarıyla orijinal metne dönüştürür."""

    sifreli_metin = base64.b64decode(b64_byte).decode('utf-8')

    orijinal_mesaj = xor_sifrele_coz(sifreli_metin, GIZLI_ANAHTAR)

    return orijinal_mesaj



# ==========================================

# 2. GÖRSEL BANNER VE ARAYÜZ BAŞLANGICI

# ==========================================



def terminali_temizle():

    os.system('cls' if os.name == 'nt' else 'clear')



def banner_yazdir():

    terminali_temizle()

    os.system('') # Windows ANSI renk desteği için

    red = "\033[31m"

    white = "\033[37m"

    cyan = "\033[36m"

    gold = "\033[33m"

    reset = "\033[0m"

    logo = f"""

{red} ███████████████████████████████████████████████████████████████

{red} █████████████████████{white}▄▄███████▄▄{red}███████████████████████████████

{red} ███████████████████{white}▄█████████████▄{red}█████████████████████████████

{red} ██████████████████{white}████████▀▀▀▀▀▀▀{red}██████████████████████████████

{red} █████████████████{white}███████▀{red}██████████████{white}▄██▄{red}████████████████████

{red} █████████████████{white}███████{red}█████████████{white}▄██████▄{red}██████████████████

{red} █████████████████{white}███████{red}█████████████{white}▀▀████▀▀{red}██████████████████

{red} █████████████████{white}███████▄{red}██████████████{white}▀██▀{red}████████████████████

{red} ██████████████████{white}████████▄▄▄▄▄▄▄{red}██████████████████████████████

{red} ███████████████████{white}▀█████████████▀{red}█████████████████████████████

{red} █████████████████████{white}▀▀███████▀▀{red}███████████████████████████████

{red} ███████████████████████████████████████████████████████████████

{white} ================================================================

{red} ██████╗ ██╗ ██╗██╗███╗ ██╗ ██████╗██╗ ██╗ ██╗ ██╗██████╗

{red} ██╔══██╗██║ ██╔╝██║████╗ ██║██╔════╝██║ ██║ ██║ ██║╚════██╗

{red} ███████║█████╔╝ ██║██╔██╗ ██║██║ ██║ ██║ ██║ ██║ █████╔╝

{red} ██╔══██║██╔═██╗ ██║██║╚██╗██║██║ ██║ ██║ ╚██╗ ██╔╝██╔═══╝

{red} ██║ ██║██║ ██╗██║██║ ╚████║╚██████╗╚██████╔╝ ╚████╔╝ ███████╗

{red} ╚═╝ ╚═╝╚═╝ ╚═╝╚═╝╚═╝ ╚═══╝ ╚═════╝ ╚═════╝ ╚═══╝ ╚══════╝

{white} ================================================================

{cyan} >> EDITED TO v2.5 : AR-GE LABORATUVAR SERİSİ <<

{gold} >> GÜVENLİK : XOR + BASE64 KRİPTO GÜVENCESİ <<

{white} ================================================================

[*] Şanlı Bayrak Altında Güvenlik Servisleri Başlatılıyor...

[*] Grafik Arayüzü (GUI) Yükleniyor, Lütfen Bekleyin...

"""

    print(logo)

    time.sleep(1.5)

    terminali_temizle()



# Program ilk açıldığında logoyu basması için çağırıyoruz

banner_yazdir()



# ==========================================

# 3. GRAFİK ARAYÜZÜ (GUI) MİMARİSİ

# ==========================================



class AkinciKriptoMuhafiz:

    def __init__(self, pencere):

        self.pencere = pencere

        self.pencere.title("AKINCI v2.5 - Kripto Muhafız")

        self.pencere.geometry("600x450")

        self.pencere.configure(bg="#0a0a0a")

        self.pencere.resizable(False, False)

      

        # Temiz ve Modern Karanlık Tema Tasarımı

        self.stil = ttk.Style()

        self.stil.theme_use("clam")

        self.stil.configure("TNotebook", background="#0a0a0a", borderwidth=0)

        self.stil.configure("TNotebook.Tab", background="#151515", foreground="#ffffff", font=("Courier", 10, "bold"), padding=[15, 5])

        self.stil.map("TNotebook.Tab", background=[("selected", "#ce1212")], foreground=[("selected", "#ffffff")])

      

        # Başlık Alanları

        ana_baslik = tk.Label(pencere, text=" AKINCI MUHAFIZ v2.5 ", font=("Courier", 22, "bold"), fg="#ce1212", bg="#0a0a0a")

        ana_baslik.pack(pady=10)

        alt_baslik = tk.Label(pencere, text="Mod: Kriptografik Güvenli Gizleme", font=("Arial", 9, "italic"), fg="#666666", bg="#0a0a0a")

        alt_baslik.pack()

      

        # Sekme Yönetimi

        self.sekme_kontrolu = ttk.Notebook(pencere)

        self.sekme_kontrolu.pack(fill="both", expand=True, padx=15, pady=15)

        self.sayfa_gizle = tk.Frame(self.sekme_kontrolu, bg="#111111")

        self.sayfa_coz = tk.Frame(self.sekme_kontrolu, bg="#111111")

        self.sekme_kontrolu.add(self.sayfa_gizle, text=" MESAJI ŞİFRELE VE GİZLE ")

        self.sekme_kontrolu.add(self.sayfa_coz, text=" GİZLİ ŞİFREYİ ÇÖZ ")

      

        # Hafızada tutulacak dosya yolları

        self.kaynak_dosya_yolu = ""

        self.cozulecek_dosya_yolu = ""

      

        self.arayuz_gizle_sayfasi()

        self.arayuz_coz_sayfasi()



    def arayuz_gizle_sayfasi(self):

        """Birinci sekmedeki elemanları oluşturur (Gizleme Ekranı)."""

        lbl_msg = tk.Label(self.sayfa_gizle, text="Gizlenecek Mesaj, Link veya Log Bilgisi:", font=("Arial", 10, "bold"), fg="#ffffff", bg="#111111")

        lbl_msg.pack(pady=10)

        self.girdi_mesaj = tk.Entry(self.sayfa_gizle, font=("Arial", 10), width=50, bg="#222222", fg="#ffffff", borderwidth=0, insertbackground="white")

        self.girdi_mesaj.pack(pady=5)

        btn_dosya = tk.Button(self.sayfa_gizle, text="Kapak Fotoğrafı Seç (.jpg/.png)", font=("Arial", 9, "bold"), bg="#333333", fg="#ffffff", command=self.dosya_sec_gizle, borderwidth=0)

        btn_dosya.pack(pady=15)

        self.lbl_durum_gizle = tk.Label(self.sayfa_gizle, text="Dosya Seçilmedi", font=("Arial", 8, "italic"), fg="#888888", bg="#111111")

        self.lbl_durum_gizle.pack()

        btn_islem = tk.Button(self.sayfa_gizle, text="KRİPTOLA VE FOTOĞRAFA GÖM", font=("Courier", 11, "bold"), bg="#ce1212", fg="#ffffff", width=30, command=self.mesaji_fotografa_gom, borderwidth=0)

        btn_islem.pack(pady=25)



    def arayuz_coz_sayfasi(self):

        """İkinci sekmedeki elemanları oluşturur (Çözme Ekranı)."""

        lbl_dec = tk.Label(self.sayfa_coz, text="İçinde Şifreli Veri Gizli Olan Dosya:", font=("Arial", 10, "bold"), fg="#ffffff", bg="#111111")

        lbl_dec.pack(pady=15)

        btn_dosya_coz = tk.Button(self.sayfa_coz, text="Analiz Edilecek Dosyayı Seç", font=("Arial", 9, "bold"), bg="#333333", fg="#ffffff", command=self.dosya_sec_coz, borderwidth=0)

        btn_dosya_coz.pack(pady=10)

        self.lbl_durum_coz = tk.Label(self.sayfa_coz, text="Dosya Seçilmedi", font=("Arial", 8, "italic"), fg="#888888", bg="#111111")

        self.lbl_durum_coz.pack(pady=5)

        btn_analiz = tk.Button(self.sayfa_coz, text="GİZLİ VERİYİ ANALİZ ET VE ÇÖZ", font=("Courier", 11, "bold"), bg="#ce1212", fg="#ffffff", width=30, command=self.gizli_mesaji_analiz_et, borderwidth=0)

        btn_analiz.pack(pady=20)

        self.girdi_sonuc = tk.Entry(self.sayfa_coz, font=("Courier", 11, "bold"), width=50, bg="#050505", fg="#00ff00", borderwidth=0, justify="center")

        self.girdi_sonuc.pack(pady=15)



    # Dosya Seçim İşlemleri

    def dosya_sec_gizle(self):

        self.kaynak_dosya_yolu = filedialog.askopenfilename(filetypes=[("Görsel Dosyaları", "*.jpg *.png *.jpeg")])

        if self.kaynak_dosya_yolu:

            self.lbl_durum_gizle.config(text=os.path.basename(self.kaynak_dosya_yolu), fg="#00ff00")



    def dosya_sec_coz(self):

        self.cozulecek_dosya_yolu = filedialog.askopenfilename(filetypes=[("Görsel Dosyaları", "*.jpg *.png *.jpeg")])

        if self.cozulecek_dosya_yolu:

            self.lbl_durum_coz.config(text=os.path.basename(self.cozulecek_dosya_yolu), fg="#00ff00")



    # ==========================================

    # 4. MANUEL DATA İŞLEME VE DOSYA YAZMA/OKUMA

    # ==========================================

  

    def mesaji_fotografa_gom(self):

        """Kullanıcının yazdığı mesajı kriptolayıp dosya sonuna ekler (EOF Steganography)."""

        try:

            mesaj = self.girdi_mesaj.get()

            if not mesaj or not self.kaynak_dosya_yolu:

                messagebox.showwarning("Eksik Bilgi", "Lütfen şifrelenecek mesajı girin ve bir kapak resmi seçin şef!")

                return

            hedef_kayit_yolu = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Formatı", "*.png")])

            if not hedef_kayit_yolu:

                return

            # Orijinal resmin ham byte'larını hafızaya alıyoruz

            with open(self.kaynak_dosya_yolu, "rb") as dosya:

                orijinal_bytes = dosya.read()

            # v2.0 Geliştirmesi: Mesajı önce XOR'layıp sonra Base64 yapıyoruz

            kriptolu_byte_verisi = metni_kriptola(mesaj)



            # Tam paket: Ayraç + Şifreli Çorba Veri + Ayraç

            gömülecek_veri = START_MARKER + kriptolu_byte_verisi + START_MARKER

            # Yeni resmi diske yazıyoruz (Orijinal resim + arkasındaki gizli paket)

            with open(hedef_kayit_yolu, "wb") as yeni_dosya:

                yeni_dosya.write(orijinal_bytes + gömülecek_veri)

            messagebox.showinfo("İşlem Başarılı", "AKINCI v2.5: Veri kriptolanarak resmin arkasına başarıyla gömüldü!")

            self.girdi_mesaj.delete(0, tk.END)

        except Exception as hata:

            messagebox.showerror("Hata Oluştu", f"Dosya yazma işlemi başarısız: {hata}")



    def gizli_mesaji_analiz_et(self):

        """Seçilen resmin byte yapısını tarar, v2 imzasını bulursa şifreyi kırıp ekrana basır."""

        try:

            if not self.cozulecek_dosya_yolu:

                messagebox.showwarning("Eksik Bilgi", "Lütfen analiz edilecek şifreli resmi seçin şef!")

                return

            with open(self.cozulecek_dosya_yolu, "rb") as dosya:

                dosya_bytes = dosya.read()

            # Dosya içinde v2.0 imzamızı arıyoruz

            if START_MARKER in dosya_bytes:

                # Byte verisini imzalara göre parçalıyoruz

                parcalar = dosya_bytes.split(START_MARKER)



                # İki imzanın ortasında kalan şifreli base64 byte verisini alıyoruz

                sifreli_b64_verisi = parcalar[1]



                # v2.0 Şifre çözme motorunu tetikliyoruz

                cozulmus_orijinal_metin = kriptolu_metni_coz(sifreli_b64_verisi)



                # Sonucu yeşil terminal alanına yazdırıyoruz

                self.girdi_sonuc.delete(0, tk.END)

                self.girdi_sonuc.insert(0, cozulmus_orijinal_metin)

                messagebox.showinfo("Başarılı Analiz", "Gizli veri yapısı deşifre edildi, şifre başarıyla kırıldı!")

            else:

                self.girdi_sonuc.delete(0, tk.END)

                self.girdi_sonuc.insert(0, "Temiz / v2.0 Yapısı Bulunamadı.")

        except Exception as hata:

            messagebox.showerror("Deşifre Hatası", f"Veri yapısı çözümlenemedi veya anahtar uyuşmadı: {hata}")



# Programın ana tetikleyicisi

if __name__ == "__main__":

    ana_ekran = tk.Tk()

    uygulama = AkinciKriptoMuhafiz(ana_ekran)

    ana_ekran.mainloop()
