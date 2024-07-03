import os
import math
import requests
from PIL import Image
from io import BytesIO

# Define the base part of the image URL
base_image_url = 'https://images.eap.bl.uk/EAP262/EAP262_1_2_35_106/1.jp2' # Ctrl + Shift + i > Search for the base imnage URL. 

# Image dimensions from the JSON data
full_width = 6854
full_height = 9678

# Tile size from the JSON data
tile_size = 256

# Calculate the number of tiles needed in each dimension
tiles_wide = math.ceil(full_width / tile_size)
tiles_high = math.ceil(full_height / tile_size)

# Set up the headers
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Create a directory for saving tiles if not exists
tiles_folder = 'tiles'
if not os.path.exists(tiles_folder):
    os.makedirs(tiles_folder)

# Function to download and return an image
def download_image(url):
    response = requests.get(url, headers=headers)
    return Image.open(BytesIO(response.content))

# Download each tile
tiles = []
for y in range(tiles_high):
    for x in range(tiles_wide):
        tile_x = x * tile_size
        tile_y = y * tile_size
        tile_width = min(tile_size, full_width - tile_x)
        tile_height = min(tile_size, full_height - tile_y)
        
        tile_url = f"{base_image_url}/{tile_x},{tile_y},{tile_width},{tile_height}/256,/0/default.jpg"
        print(f"Downloading tile: {tile_url}")
        
        img = download_image(tile_url)
        tile_path = os.path.join(tiles_folder, f"tile_{x}_{y}.jpg")
        img.save(tile_path)
        tiles.append((tile_x, tile_y, img))

# Create directory for full image if it doesn't exist
image_folder = 'high_res_images'
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# Create a new image with the correct dimensions
full_image = Image.new('RGB', (full_width, full_height))

# Place each tile in the correct position
for x, y, img in tiles:
    full_image.paste(img, (x, y))

# Save the full image
full_image_path = os.path.join(image_folder, 'Page1_full_high_res.jpg')
full_image.save(full_image_path)
print(f"Saved full image at {full_image_path}")

print("DONE!")