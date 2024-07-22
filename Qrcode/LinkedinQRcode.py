#!/usr/bin/env python3
"""Making a hippo qrcode"""

import qrcode
from PIL import Image

# Create a QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data('https://www.linkedin.com/in/cathyaugustin/')
qr.make(fit=True)

# Create a QR code image
img_qr = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Import hippo imae
img_hippocampe = Image.open('CM.png')

# Check image mode
if img_hippocampe.mode == 'RGBA':
    # Use alpha canal for image
    mask = img_hippocampe.split()[3]  # The alpha channel is the 4th channel in 'RGBA'.
else:
    # Convert image to grayscale for use as mask
    mask = img_hippocampe.convert('L')

# Resize the seahorse image to fit the QR Code
width, height = img_qr.size
img_hippocampe = img_hippocampe.resize((int(width * 0.3), int(height * 0.3)))
mask = mask.resize((int(width * 0.3), int(height * 0.3)))

# Calculate the position to center the image of the hippocampus on the QR Code
position = ((width - img_hippocampe.width) // 2, (height - img_hippocampe.height) // 2)

# Paste the seahorse onto the QR Code using the appropriate mask
img_qr.paste(img_hippocampe, position, mask)

# Save final image
img_qr.save('qrcode_linkedin.png')

# Display image
img_qr.show()
