<div align="center">

# 🕐 Digital Clock — Dark Red Edition

**Jam digital desktop minimalis dengan estetika gelap bernuansa merah membara.**
Dibangun murni dengan Python & Tkinter — ringan, tanpa dependensi eksternal.

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-red?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-informational?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</div>

---

## ✨ Preview

<div align="center">

```
┌──────────────────────────────────────┐
│                                       │
│            14:27:53                  │
│      Wednesday, 29 July 2026         │
│                                       │
│         [ Format: 24 Jam ]           │
│                                       │
└──────────────────────────────────────┘
```

*Kartu gelap dengan aksen merah menyala (`#ff3b30`) di atas latar hitam pekat (`#0c0000`) — terinspirasi dari tampilan jam digital bergaya neon/retro.*

</div>

> 💡 Ganti blok di atas dengan screenshot asli aplikasi (`assets/preview.png`) agar README makin hidup.

---

## 📖 Tentang Proyek

**Digital Clock** adalah aplikasi jam digital desktop yang dirancang dengan fokus pada **tampilan visual yang estetis**, bukan sekadar fungsi menampilkan waktu. Proyek ini menonjolkan:

- Palet warna gelap yang konsisten dan disengaja (bukan warna default Tkinter)
- Efek **kedip pada titik dua** (`:`) setiap detik, meniru jam digital fisik
- Dukungan **font kustom** (mis. *Bebas Neue*) yang otomatis dimuat di Windows jika tersedia
- Toggle format waktu **12 Jam ⇄ 24 Jam** langsung dari UI

---

## 🎯 Fitur Utama

| Fitur | Deskripsi |
|---|---|
| 🕒 **Real-time clock** | Update setiap 1 detik menggunakan `root.after()`, tanpa threading tambahan |
| 🔁 **Toggle 12/24 Jam** | Satu klik tombol untuk berpindah format waktu |
| ✨ **Efek kedip** | Titik dua (`:`) berkedip setiap detik untuk kesan "hidup" |
| 📅 **Tanggal lengkap** | Menampilkan hari, tanggal, bulan, dan tahun secara otomatis |
| 🎨 **Auto font-fallback** | Mencoba deretan font "digital-look" (Bebas Neue → Oswald → Anton → Digital-7 → ... → Courier New) |
| 🪟 **Font loader Windows** | Memuat file `.ttf` custom secara privat via `ctypes` (tidak perlu install font ke sistem) |
| 🖥️ **Window terpusat otomatis** | Ukuran jendela `560x260` selalu muncul di tengah layar |
| 🚫 **Fixed size window** | Ukuran dikunci (`resizable(False, False)`) untuk menjaga proporsi desain |

---

## 🎨 Palet Warna

Desain menggunakan skema warna kustom bertema *"cherry cola meets embers"*:

| Nama Variabel | Kode Hex | Kegunaan |
|---|---|---|
| `BG_UTAMA` | `#0c0000` | Latar belakang jendela utama |
| `BG_KARTU` | `#150202` | Latar kartu/panel |
| `AKSEN` | `#ff3b30` | Warna teks jam & tombol (merah terang) |
| `AKSEN_REDUP` | `#4a1210` | Aksen redup (cadangan/hover) |
| `TEKS_TANGGAL` | `#7a2c28` | Warna teks tanggal |
| `GARIS_TEPI` | `#331010` | Border/outline kartu |

---

## 🛠️ Teknologi yang Digunakan

- **Python 3.8+**
- **Tkinter** — GUI bawaan Python (tidak perlu instalasi tambahan)
- **ctypes** — untuk memuat font kustom secara privat di Windows
- **time.strftime** — untuk formatting waktu & tanggal

---

## 🚀 Instalasi & Menjalankan

### Prasyarat
Pastikan Python 3.8 ke atas sudah terpasang:

```bash
python --version
```

> Tkinter biasanya sudah termasuk dalam instalasi Python standar. Jika belum ada (khususnya di Linux), install dengan:
> ```bash
> sudo apt-get install python3-tk
> ```

### Clone repository

```bash
git clone https://github.com/username/digital-clock.git
cd digital-clock
```

### Jalankan aplikasi

```bash
python digital_clock.py
```

Selesai — jendela jam digital akan langsung muncul di tengah layar. 🎉

---

## ✍️ (Opsional) Menambahkan Font Kustom

Untuk mendapatkan tampilan digital yang lebih maksimal, letakkan salah satu file berikut di folder yang sama dengan `digital_clock.py`:

```
BebasNeue-Regular.ttf
BebasNeue.ttf
Bebas Neue.ttf
```

Aplikasi akan otomatis mendeteksi dan memuat font tersebut secara privat **hanya di Windows** (via `AddFontResourceExW`) — tanpa perlu install font ke seluruh sistem. Jika tidak ditemukan, aplikasi akan otomatis jatuh ke font fallback berikutnya di daftar kandidat (`Oswald`, `Anton`, dst.) hingga akhirnya ke `Courier New`.

---

## 📁 Struktur Proyek

```
digital-clock/
├── digital_clock.py         # Kode utama aplikasi
├── BebasNeue-Regular.ttf    # (opsional) font kustom
└── README.md
```

---

## 🧩 Struktur Kode Singkat

| Fungsi/Class | Peran |
|---|---|
| `muat_font_khusus_windows()` | Memuat font `.ttf` kustom secara privat, khusus platform Windows |
| `pilih_font_digital(root)` | Memilih font terbaik yang tersedia dari daftar kandidat |
| `DigitalClock` | Class utama: mengatur jendela, tampilan (kartu, label jam/tanggal, tombol), dan loop update jam setiap detik |

---

## 💡 Catatan & Ide Pengembangan

- Nama hari dan bulan (`%A`, `%B` pada `strftime`) mengikuti **locale sistem** — secara default akan tampil dalam Bahasa Inggris. Untuk menampilkan dalam Bahasa Indonesia, tambahkan di awal program:
  ```python
  import locale
  locale.setlocale(locale.LC_TIME, "id_ID.UTF-8")  # Linux/macOS
  # atau "Indonesian_Indonesia.1252" di Windows
  ```
- Ide pengembangan lanjutan:
  - [ ] Mode alarm / stopwatch
  - [ ] Tema warna alternatif (dark/light toggle)
  - [ ] Opsi "always on top"
  - [ ] Dukungan multi-zona waktu

---

## 🤝 Kontribusi

Kontribusi, saran, dan *pull request* sangat terbuka! Untuk perubahan besar, silakan buka *issue* terlebih dahulu untuk mendiskusikan apa yang ingin diubah.

1. Fork repository ini
2. Buat branch baru (`git checkout -b fitur-baru`)
3. Commit perubahan (`git commit -m 'Menambahkan fitur X'`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buka Pull Request

---

## 📜 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE) — bebas digunakan, dimodifikasi, dan didistribusikan.

---

<div align="center">

Dibuat dengan 🔥 dan secangkir kopi oleh **Dava**

</div>
