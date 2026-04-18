import qrcode
import matplotlib.pyplot as plt

# -------- QR 1: Image Link --------
img1 = qrcode.make("https://images.pexels.com/photos/236047/pexels-photo-236047.jpeg")
img1.save("image_qr.png")

# -------- QR 2: Text --------
img2 = qrcode.make("Hello Shravani! QR is working ✅")
img2.save("text_qr.png")

# -------- Display --------
plt.imshow(img1)
plt.axis('off')
plt.title("QR for Image Link")
plt.show()

plt.imshow(img2)
plt.axis('off')
plt.title("QR for Text")
plt.show()

print("QR codes generated successfully!")
