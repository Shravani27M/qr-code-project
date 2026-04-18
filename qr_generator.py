import qrcode
import matplotlib.pyplot as plt

# QR for image link
img1 = qrcode.make("https://images.pexels.com/photos/236047/pexels-photo-236047.jpeg")
img1.save("image_qr.png")

# QR for text
img2 = qrcode.make("Hello, you are learning QR code!")
img2.save("text_qr.png")

# Display both
plt.imshow(img1)
plt.axis('off')
plt.show()

plt.imshow(img2)
plt.axis('off')
plt.show()
