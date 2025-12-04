import cv2
import numpy as np
import pyvirtualcam
from pyvirtualcam import PixelFormat

current_mode = 2
mode_names = {1: "Klasik Siluet", 2: "Matrix / TRON Modu", 3: "Renkli Eskiz"}

# Ghost Effect Variables
ghost_mode = True
prev_frame = None


def empty(a): pass


cv2.namedWindow("Siluet Ayarlari")
cv2.resizeWindow("Siluet Ayarlari", 600, 150)
cv2.createTrackbar("Detay Seviyesi (Alt)", "Siluet Ayarlari", 50, 255, empty)
cv2.createTrackbar("Ana Hatlar (Ust)", "Siluet Ayarlari", 150, 255, empty)
cv2.createTrackbar("Cizgi Kalinligi", "Siluet Ayarlari", 2, 5, empty)  # Kalinlik 2 daha iyi durur
cv2.createTrackbar("Iz Uzunlugu", "Siluet Ayarlari", 10, 50, empty)  # Izin ne kadar kalacagi

cap = cv2.VideoCapture(0)
width = 640
height = 480
cap.set(3, width)
cap.set(4, height)

prev_frame = np.zeros((height, width, 3), np.uint8)

print("Kamera baslatiliyor... Gorsel sov icin haziriz.")

with pyvirtualcam.Camera(width=width, height=height, fps=30, fmt=PixelFormat.BGR) as cam:
    while True:
        success, img = cap.read()
        if not success:
            break

        img = cv2.flip(img, 1) #Aynalama/Mirroring
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)

        t1 = cv2.getTrackbarPos("Detay Seviyesi (Alt)", "Siluet Ayarlari")
        t2 = cv2.getTrackbarPos("Ana Hatlar (Ust)", "Siluet Ayarlari")
        thickness = cv2.getTrackbarPos("Cizgi Kalinligi", "Siluet Ayarlari")
        decay_val = cv2.getTrackbarPos("Iz Uzunlugu", "Siluet Ayarlari")

        if decay_val == 0: decay_val = 1

        imgCanny = cv2.Canny(imgBlur, t1, t2)

        if thickness > 0:
            kernel = np.ones((thickness, thickness), np.uint8)
            imgCanny = cv2.dilate(imgCanny, kernel, iterations=1)

        processed_frame = None

        if current_mode == 1:  #Classic
            processed_frame = cv2.cvtColor(imgCanny, cv2.COLOR_GRAY2BGR)

        elif current_mode == 2:  #Matrix Effect
            matrix_bg = np.zeros_like(img)
            matrix_bg[imgCanny > 0] = (0, 255, 0)
            processed_frame = matrix_bg

        elif current_mode == 3: 
            imgInverted = cv2.bitwise_not(imgCanny)
            processed_frame = cv2.cvtColor(imgInverted, cv2.COLOR_GRAY2BGR)

        # --- YENI GELISMIS GHOST EFEKTI ---
        final_output = processed_frame

        if ghost_mode:
            subtraction_matrix = np.ones_like(prev_frame) * (55 - decay_val)
            prev_frame_decayed = cv2.subtract(prev_frame, subtraction_matrix)
            final_output = cv2.max(processed_frame, prev_frame_decayed)
        prev_frame = final_output

        #Arayüz Detayları - Interface Details
        cv2.putText(final_output, f"", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (200, 200, 200), 2)
        status_text = "" if ghost_mode else ""
        col = (0, 255, 0) if ghost_mode else (0, 0, 255)
        cv2.putText(final_output, f"{status_text}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, col, 2)

        cam.send(final_output)
        cv2.imshow("Kamera Onizleme", final_output)

        cam.sleep_until_next_frame()

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('1'):
            current_mode = 1
        elif key == ord('2'):
            current_mode = 2
        elif key == ord('3'):
            current_mode = 3
        elif key == ord('g') or key == ord('G'):
            ghost_mode = not ghost_mode
            if not ghost_mode: prev_frame = np.zeros((height, width, 3), np.uint8)

cap.release()
cv2.destroyAllWindows()
