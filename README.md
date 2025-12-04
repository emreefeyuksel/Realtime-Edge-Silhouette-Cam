# 🥷 Real-time Edge Silhouette Cam

<div align="center">
  <a href="#-english">🇺🇸 <strong>English</strong></a> | 
  <a href="#-türkçe">🇹🇷 <strong>Türkçe</strong></a>
</div>

<div align="center">
  <br>
</div>

---

<a name="-english"></a>
## 🇺🇸 English

**Real-time Edge Silhouette Cam** is a Python application that turns your webcam feed into a stylish, high-contrast silhouette using edge detection algorithms (Canny). 

Unlike standard image processing scripts, **this project streams the processed video directly to a virtual camera driver**. This means you can use this silhouette effect as your actual camera in **Discord, Google Meet, Zoom, or OBS** without needing screen capture.

### 🌟 Key Features
* **Virtual Camera Support:** Acts as a real webcam device (Selectable in Discord/Zoom/Meet).
* **Privacy Focused:** Hides your face and background details, showing only outlines.
* **Real-Time Controls:** Adjust edge sensitivity (thresholds) and line thickness on the fly using trackbars.
* **Cyberpunk Aesthetic:** Creates a unique "hacker" or "ghost" visual style.

### 🛠 Tech Stack
* **Python 3.x**
* **OpenCV** (Image Processing & Canny Edge Detection)
* **pyvirtualcam** (Streaming frames to the virtual camera driver)
* **NumPy** (Matrix operations)

### 🚀 Installation

1.  **Prerequisite (Important):** You need a virtual camera driver installed. The easiest way is to install **OBS Studio** (which comes with OBS Virtual Camera). You don't need to run OBS, just having it installed is enough for the driver to exist.

2.  **Clone the repository:**
    ```bash
    git clone [https://github.com/emreefeyuksel/Realtime-Edge-Silhouette-Cam.git](https://github.com/emreefeyuksel/Realtime-Edge-Silhouette-Cam.git)
    cd Realtime-Edge-Silhouette-Cam
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### 🎮 Usage

1.  Run the script:
    ```bash
    python main.py
    ```
2.  A window named **"Siluet Ayarlari"** will appear.
3.  Open your meeting app (Discord, Google Meet, Zoom, etc.).
4.  Go to **Camera Settings** and select **"OBS Virtual Camera"** (or UnityCam) as your video source.
5.  Enjoy your new look! Use the sliders to adjust the detail level.

* **'g':** Ghost mode on/off.
* **'q':** Quit the application.

---

<a name="-türkçe"></a>
## 🇹🇷 Türkçe

**Real-time Edge Silhouette Cam**, webcam görüntünüzü kenar algılama algoritmaları (Canny) kullanarak anlık olarak stilize edilmiş bir silüete dönüştüren bir Python uygulamasıdır.

Sıradan görüntü işleme projelerinden farklı olarak, **işlenmiş görüntüyü doğrudan sanal kamera sürücüsüne gönderir**. Bu sayede **Discord, Google Meet, Zoom veya OBS** gibi uygulamalarda, ekran paylaşımı yapmaya gerek kalmadan bu efekti ana kameranız olarak kullanabilirsiniz.

### 🌟 Temel Özellikler
* **Sanal Kamera Desteği:** Gerçek bir webcam gibi davranır (Discord/Zoom/Meet ayarlarından seçilebilir).
* **Gizlilik Odaklı:** Yüzünüzü ve arka plan detaylarını gizler, sadece hatları gösterir.
* **Anlık Kontrol:** Detay seviyesini ve çizgi kalınlığını uygulama çalışırken kaydırma çubuklarıyla ayarlayabilirsiniz.
* **Cyberpunk Tarzı:** Eşsiz, "hacker" veya "hayalet" benzeri bir görsel tarz oluşturur.

### 🛠 Kullanılan Teknolojiler
* **Python 3.x**
* **OpenCV** (Görüntü İşleme ve Canny Algoritması)
* **pyvirtualcam** (Görüntüyü sanal kamera sürücüsüne aktarma)
* **NumPy** (Matris işlemleri)

### 🚀 Kurulum

1.  **Ön Hazırlık (Önemli):** Bilgisayarınızda bir sanal kamera sürücüsü yüklü olmalıdır. En kolay yol **OBS Studio**'yu kurmaktır (içinde OBS Virtual Camera ile gelir). OBS uygulamasını açmanıza gerek yoktur, yüklü olması yeterlidir.

2.  **Projeyi indirin:**
    ```bash
    git clone [https://github.com/emreefeyuksel/Realtime-Edge-Silhouette-Cam.git](https://github.com/emreefeyuksel/Realtime-Edge-Silhouette-Cam.git)
    cd Realtime-Edge-Silhouette-Cam
    ```

3.  **Gerekli kütüphaneleri yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

### 🎮 Kullanım

1.  Uygulamayı başlatın:
    ```bash
    python main.py
    ```
2.  Ekranda **"Siluet Ayarlari"** penceresi açılacaktır.
3.  Toplantı uygulamanızı açın (Discord, Google Meet, vb.).
4.  **Kamera Ayarları**'na gidin ve kaynak olarak **"OBS Virtual Camera"**yı seçin.
5.  Yeni görüntünüzün keyfini çıkarın! Detayları ayarlamak için kaydırma çubuklarını kullanın.

* **'g':** Ghost modu aç/kapat.
* **'q':** Çıkış yapmak için basın.

---
<div align="center">
  Developed by <a href="https://github.com/emreefeyuksel">Emre Efe Yüksel</a>
</div>
