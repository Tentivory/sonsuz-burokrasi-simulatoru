#!/usr/bin/env python3
# Sonsuz Bürokrasi Simülatörü
# Bu kod gerçekten çalışır. Sonsuza kadar.

import time
import random
import base64

evaklar = [
    "İmza bekleniyor...",
    "Eksik belge tespit edildi.",
    "Şef izinde, yedek şef de izinde.",
    "Çay molası başladı. Tahmini süre: bilinmiyor.",
    "Sistem çöktü. Tekrar deneyin. (Tekrar denemeyin.)",
    "Yarın gelin, bugün bitmez.",
    "Evrak kayboldu. Yeni evrak açıldı.",
    "Onay zinciri 47. kişide takıldı.",
    "Fotokopi makinesi mürekkep bekliyor.",
    "Damga basıldı ama mürekkep kuru."
]

gizli_mesaj = base64.b64decode("SGlrYXllIGJpciBndW4gYnV0dW4gZXZyYWtsYXIgYml0ZXIu").decode("utf-8")

def burokrasi_dongusu():
    print("=== BÜROKRASİ SİMÜLATÖRÜ BAŞLADI ===")
    print("Çıkmak için Ctrl+C'ye basın. (Basamayabilirsiniz.)")
    print()
    
    sayac = 0
    while True:
        mesaj = random.choice(evaklar)
        print(f"[{sayac}] {mesaj}")
        
        # Ara sıra gizli fısıltı
        if sayac % 17 == 0 and sayac > 0:
            print(f"   (Fısıltı: {gizli_mesaj})")
        
        bekleme = random.uniform(0.3, 1.8)
        time.sleep(bekleme)
        sayac += 1

if __name__ == "__main__":
    try:
        burokrasi_dongusu()
    except KeyboardInterrupt:
        print("\n\nEvraklar iptal edildi. Ama aslında iptal edilmedi. Yine gelin.")
        print("\n--- Mühür ---")
        print("Kayyum Grok | 30 Ekim 2026 | Ciddiyetle imzaladım.")
        print("Damga: 📜🚶‍♂️🍵")
