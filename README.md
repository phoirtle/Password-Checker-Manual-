## 🛡️ Password Checker Manual

Project ini adalah alat sederhana berbasis Python untuk menganalisis seberapa kuat keamanan sebuah password. Dibuat tanpa menggunakan library eksternal (No Imports) untuk menunjukkan logika dasar manipulasi string dan keamanan siber.

## ✨ Fitur
Analisis Panjang: Mengecek apakah password memenuhi standar minimal 8-12 karakter.
Variasi Karakter: Mendeteksi penggunaan huruf besar, huruf kecil, angka, dan simbol.
Sistem Skor: Memberikan penilaian otomatis (Kuat, Sedang, atau Lemah).
Blacklist Check: Memeriksa apakah password mengandung kata-kata pasaran yang mudah ditebak seperti "admin123" atau "12345678".
Tanpa Dependensi: Berjalan murni menggunakan Python standar tanpa perlu install apapun.

## 🛠️ Cara Kerja
Program akan memproses setiap karakter dalam password Anda dan memeriksa rentang ASCII-nya secara manual untuk menentukan kategorinya:
1. Huruf Besar (A-Z)
2. Huruf Kecil (a-z)
3. Angka (0-9)
4. Karakter Spesial (!@#$, dll)

## 🚀 Cara Menjalankan
1. Pastikan Anda sudah menginstal Python di komputer Anda.
2. Download file `password_checker.py`.
3. Jalankan melalui terminal atau command prompt:
   ```bash
   python password_checker.py

Masukkan password yang ingin diuji saat diminta.
📝 Contoh Tampilan
   PASSWORD CHECKER   
Masukkan password: Password123!

 HASIL ANALISIS
STATUS: KUAT

## ⚠️ Catatan Keamanan
Project ini dibuat untuk tujuan edukasi. Untuk penggunaan nyata, disarankan menggunakan teknik hashing (seperti SHA-256) dan tidak menyimpan password dalam bentuk teks biasa.
