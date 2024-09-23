from captcha.image import ImageCaptcha
import random

# Set a random seed (optional)
random.seed(42)

image = ImageCaptcha(width=450, height=100)

def generate_random_captcha_text(length=6):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    captcha_text = ''.join(random.choice(characters) for _ in range(length)) 
    return captcha_text

# Get random captcha text
captcha_text = generate_random_captcha_text()

# Generate the image of the given text
data = image.generate(captcha_text)

# Write the image on the given file and save it 
image.write(captcha_text, 'CAPTCHA1.png')


from PIL import Image 
Image.open('CAPTCHA1.png').show()