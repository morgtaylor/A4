from PIL import Image
import random
import time

def counting_sort(colors, channel):
    count = [0] * 256
    output = [0] * len(colors)
    for color in colors:
        count[color[channel]] += 1
    for i in range(1, 256):
        count[i] += count[i - 1]
    for color in reversed(colors):
        output[count[color[channel]] - 1] = color
        count[color[channel]] -= 1
    return output

def merge_sort(colors):
    if len(colors) > 1:
        mid = len(colors) // 2
        left_half = colors[:mid]
        right_half = colors[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                colors[k] = left_half[i]
                i += 1
            else:
                colors[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            colors[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            colors[k] = right_half[j]
            j += 1
            k += 1

def generate_image(size):
    # Generate a list of random RGB pixel colors
    pixels = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(size[0] * size[1])]
    return pixels

def show_image(pixels, size):
    img = Image.new('RGB', size)
    img.putdata(pixels)
    return img

n = 1
image_size = (500, 500)
print(f"{n:10} images    linear (ms)   merge (ms)")
while n <= 100: 
    images = [generate_image(image_size) for _ in range(n)]

    # original_image = show_image(images[0], image_size)
    # original_image.show(title="Original Image")

    start_time = time.perf_counter()
    for img_pixels in images:
        sorted_pixels = counting_sort(img_pixels, 0)
        sorted_pixels = counting_sort(sorted_pixels, 1)
        sorted_pixels = counting_sort(sorted_pixels, 2)
    linear_time = (time.perf_counter() - start_time) * 1000  # Time in milliseconds

    start_time = time.perf_counter()
    for img_pixels in images:
        merge_sort(img_pixels)  # Sort by RGB tuple using merge sort
    merge_time = (time.perf_counter() - start_time) * 1000  # Time in milliseconds

    # sorted_image = show_image(sorted_pixels, image_size)
    # sorted_image.show(title="Sorted Image")

    print(f"{n:10} images  {linear_time:10.3f}ms  {merge_time:10.3f}ms")
    n = n * 2