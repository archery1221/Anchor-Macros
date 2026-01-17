# Anchor-Macros
Anchor Macro
Ne İşe Yarar?

Bu script, R tuşuna bastığında sırasıyla:

Anchor

Glowstone (belli ihtimalle)

Totem
kullanır ve sağ tık atar.
Minecraft PvP (Anchor / Crystal tarzı) için yapılmıştır.

Gereksinimler

Python 3.x

Gerekli kütüphaneler:

pip install pyautogui pynput

Tuş Ayarları (ÖNEMLİ)

Aşağıdaki satırı kendi tuşlarına göre değiştir:

for b1 in ['x', 'v', '"']:


x → Anchor tuşu

v → Glowstone tuşu

" → Totem tuşu

Glowstone basma ihtimali:

if b1 == 'v' and random.random() < 0.25:


➡ %25 ihtimal.
Değiştirmek için 0.25 değerini ayarla.

Kullanım

Scripti çalıştır

Oyuna gir

R tuşuna bas

Macro devreye girer
Sorumluluk Reddi

Macro kötüye kullanılırsa sorumluluk bana ait değil.

Sunucu banı vs. senin problemin.

Script olduğu gibi verilir, garanti yok.
