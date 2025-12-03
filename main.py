import cv2
import numpy as np
import pyvirtualcam
from pyvirtualcam import PixelFormat


# Trackbar boş fonksiyonu
def empty(a):
    pass


# Ayar Penceresi
cv2.namedWindow("Siluet Ayarlari")
cv2.resizeWindow("Siluet Ayarlari", 640, 100)
cv2.createTrackbar("Detay Seviyesi (Alt)", "Siluet Ayarlari", 50, 255, empty)
cv2.createTrackbar("Ana Hatlar (Ust)", "Siluet Ayarlari", 150, 255, empty)
cv2.createTrackbar("Cizgi Kalinligi", "Siluet Ayarlari", 1, 5, empty)

# Webcam başlat
cap = cv2.VideoCapture(0)
width = 640
height = 480
cap.set(3, width)
cap.set(4, height)

# Sanal Kamera Başlatma (OBS Virtual Camera sürücüsünü hedefler)
print("Sanal Kamera baslatiliyor... Discord'da 'OBS Virtual Camera'yi sec.")

with pyvirtualcam.Camera(width=width, height=height, fps=30, fmt=PixelFormat.BGR) as cam:
    while True:
        success, img = cap.read()
        if not success:
            break

        # Aynala
        img = cv2.flip(img, 1)

        # İşlemler (Gri -> Blur -> Canny)
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)

        t1 = cv2.getTrackbarPos("Detay Seviyesi (Alt)", "Siluet Ayarlari")
        t2 = cv2.getTrackbarPos("Ana Hatlar (Ust)", "Siluet Ayarlari")
        thickness = cv2.getTrackbarPos("Cizgi Kalinligi", "Siluet Ayarlari")

        imgCanny = cv2.Canny(imgBlur, t1, t2)

        if thickness > 1:
            kernel = np.ones((thickness, thickness), np.uint8)
            imgCanny = cv2.dilate(imgCanny, kernel, iterations=1)

        # Canny -> BGR
        final_output = cv2.cvtColor(imgCanny, cv2.COLOR_GRAY2BGR)

        # Görüntüyü sanal kameraya gönder
        cam.send(final_output)
        cv2.imshow("Siluet Ayarlari", final_output)

        # Kameranın FPS'ini senkronize et
        cam.sleep_until_next_frame()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()