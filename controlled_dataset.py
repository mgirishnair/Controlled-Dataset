import os
from PIL import Image, ImageDraw
import random

def draw_triangle(draw, center, size, color, orientation='up'):
    x, y = center
    if orientation == 'up':
        points = [(x, y - size), (x - size, y + size), (x + size, y + size)]
    elif orientation == 'down':
        points = [(x, y + size), (x - size, y - size), (x + size, y - size)]
    elif orientation == 'left':
        points = [(x - size, y), (x + size, y - size), (x + size, y + size)]
    elif orientation == 'right':
        points = [(x + size, y), (x - size, y - size), (x - size, y + size)]
    draw.polygon(points, fill=color)

def generate_triangle_dataset(output_dir, num_images=100):
    os.makedirs(output_dir, exist_ok=True)
    valid_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    orientations = ['up', 'down', 'left', 'right']
    img_size = (100, 100)
    triangle_size = 10
    positions = [(25, 50), (50, 50), (75, 50)]

    data = []

    for i in range(num_images):
        img = Image.new("RGB", img_size, (255, 255, 255))
        draw = ImageDraw.Draw(img)
        is_valid = random.choice([True, False])

        if is_valid:
            colors = valid_colors
            orientation = random.choice(orientations)
            for pos, color in zip(positions, colors):
                draw_triangle(draw, pos, triangle_size, color, orientation)
            if random.choice([True, False]):
                angle = random.uniform(-360, 360)
                img = img.rotate(angle, expand=True, fillcolor=(255, 255, 255))
        else:
            colors = valid_colors.copy()
            random.shuffle(colors)
            orientations_sample = [random.choice(orientations) for _ in range(3)]
            for pos, color, ori in zip(positions, colors, orientations_sample):
                draw_triangle(draw, pos, triangle_size, color, ori)

        label = 1 if is_valid else 0
        filename = f"img_{i:04d}_label_{label}.png"
        img.save(os.path.join(output_dir, filename))
        data.append((filename, label))

    return data


output_dir = "D:\\Delft\\Uni\\Mod 4\\Research in MLDL\\Controlled dataset\\dataset"
dataset_info = generate_triangle_dataset(output_dir, num_images=500)


