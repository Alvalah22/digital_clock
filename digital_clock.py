import os
import ctypes
import tkinter as tk
from tkinter import font as tkfont
from time import strftime

def muat_font_khusus_windows():
    if os.name != "nt":
        return 

    folder_script = os.path.dirname(os.path.abspath(__file__))
    kemungkinan_nama_file = ("BebasNeue-Regular.ttf", "BebasNeue.ttf", "Bebas Neue.ttf")

    for nama_file in kemungkinan_nama_file:
        path_font = os.path.join(folder_script, nama_file)
        if os.path.exists(path_font):
            FR_PRIVATE = 0x10  
            ctypes.windll.gdi32.AddFontResourceExW(path_font, FR_PRIVATE, 0)
            return

def pilih_font_digital(root):
    kandidat = [
            "Bebas Neue", "Oswald", "Anton",
            "Digital-7", "DS-Digital", "Segment7",
            "Consolas", "Courier New",
        ]
    keluarga_tersedia = set(tkfont.families(root))
    for nama in kandidat:
        if nama in keluarga_tersedia:
            return nama
    return "Courier New"

class DigitalClock:
    BG_UTAMA     = "#0c0000"   
    BG_KARTU     = "#150202"  
    AKSEN        = "#ff3b30"  
    AKSEN_REDUP  = "#4a1210" 
    TEKS_TANGGAL = "#7a2c28" 
    GARIS_TEPI   = "#331010"

    def __init__(self, root):
            self.root = root
            self.mode_24_jam = True  
            self.kedip_on = True      

            self._siapkan_jendela()
            self._siapkan_tampilan()
            self._jalankan_jam() 

    def _siapkan_jendela(self):
            self.root.title("Digital Clock")
            self.root.configure(bg=self.BG_UTAMA)
            self.root.resizable(False, False)
    
            lebar, tinggi = 560, 260
            layar_w = self.root.winfo_screenwidth()
            layar_h = self.root.winfo_screenheight()
            x = (layar_w // 2) - (lebar // 2)
            y = (layar_h // 2) - (tinggi // 2)
            self.root.geometry(f"{lebar}x{tinggi}+{x}+{y}")

    def _siapkan_tampilan(self):
            font_digital = pilih_font_digital(self.root)
    
            kartu = tk.Frame(
                self.root,
                bg=self.BG_KARTU,
                highlightbackground=self.GARIS_TEPI,
                highlightthickness=1,
            )
            kartu.pack(padx=28, pady=28, fill="both", expand=True)
    
            self.label_jam = tk.Label(
                kartu,
                font=(font_digital, 62, "bold"),
                bg=self.BG_KARTU,
                fg=self.AKSEN,
            )
            self.label_jam.pack(pady=(28, 4))
    
            self.label_tanggal = tk.Label(
                kartu,
                font=("Segoe UI", 13),
                bg=self.BG_KARTU,
                fg=self.TEKS_TANGGAL,
            )
            self.label_tanggal.pack(pady=(0, 18))
    
            self.tombol_format = tk.Button(
                kartu,
                text="Format: 24 Jam",
                font=("Segoe UI", 10, "bold"),
                bg=self.BG_KARTU,
                fg=self.AKSEN,
                activebackground=self.AKSEN,
                activeforeground=self.BG_KARTU,
                relief="solid",
                bd=1,
                highlightbackground=self.AKSEN,
                padx=14,
                pady=6,
                cursor="hand2",
                command=self._ganti_format_jam,
            )
            self.tombol_format.pack(pady=(0, 20))
            self.tombol_format.bind("<Enter>", self._saat_hover_masuk)
            self.tombol_format.bind("<Leave>", self._saat_hover_keluar)

    def _saat_hover_masuk(self, event):
        self.tombol_format.config(bg=self.AKSEN, fg=self.BG_KARTU)
    
    def _saat_hover_keluar(self, event):
        self.tombol_format.config(bg=self.BG_KARTU, fg=self.AKSEN)

    def _ganti_format_jam(self):
        self.mode_24_jam = not self.mode_24_jam
        teks_tombol = "Format: 24 Jam" if self.mode_24_jam else "Format: 12 Jam"
        self.tombol_format.config(text=teks_tombol)        

    def _jalankan_jam(self):
            pola_jam = "%H:%M:%S" if self.mode_24_jam else "%I:%M:%S %p"
            teks_jam = strftime(pola_jam)

            if not self.kedip_on:
                teks_jam = teks_jam.replace(":", " ")
            self.kedip_on = not self.kedip_on
    
            teks_tanggal = strftime("%A, %d %B %Y")  
    
            self.label_jam.config(text=teks_jam)
            self.label_tanggal.config(text=teks_tanggal)
    
            self.root.after(1000, self._jalankan_jam)
    
if __name__ == "__main__":
    muat_font_khusus_windows() 
    root = tk.Tk()
    app = DigitalClock(root)
    root.mainloop()