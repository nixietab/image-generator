import random
import os
from PIL import Image

def generate_random_image(size):
    image = Image.new("RGB", (size, size))

    pixels = []
    for _ in range(size * size):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        pixels.append((red, green, blue))

    image.putdata(pixels)
    return image

if __name__ == "__main__":
    sizes = [64, 32, 16, 8, 4, 2, 1]
    for size in sizes:
        filename = f"r{size}x{size}.png"
        random_image = generate_random_image(size)

        scaled_image = random_image.resize((256, 256), resample=Image.NEAREST)
        scaled_filename = f"r{size}x{size}.png"
        scaled_image.save(scaled_filename)
        print(f"Random image generated with size {size}x{size}, pixel-perfectly rescaled to 256x256, and saved as '{scaled_filename}'")
