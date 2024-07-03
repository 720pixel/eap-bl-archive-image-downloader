
# EAP BL Image Downloader

This Python script downloads high-resolution images by stitching together multiple image tiles from a specified base URL. The script is designed to handle large images by dividing them into smaller tiles, downloading each tile, and then reassembling them into the full image.

## Features

- Downloads image tiles from a specified base URL.
- Stitches the downloaded tiles into a high-resolution image.
- Saves both the individual tiles and the final stitched image.

## Requirements

- Python 3.x
- PIL (Pillow)
- Requests

You can install the required packages using pip:

```bash
pip install pillow requests
```

## Usage

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/eap-bl-image-downloader.git
    cd eap-bl-image-downloader
    ```

2. **Edit the script**: Update the `base_image_url` variable with the base URL of the image you want to download. This URL should be obtained from the web page by inspecting the network requests or source code.

    ```python
    base_image_url = 'https://images.eap.bl.uk/EAP262/EAP262_1_2_35_106/1.jp2'  # Example URL
    ```

3. **Run the script**:

    ```bash
    python eap-bl-image-downloader.py
    ```

4. **Find the output**: The individual tiles will be saved in the `tiles` directory, and the final high-resolution image will be saved in the `high_res_images` directory.

## Script Details

The script performs the following steps:

1. **Calculate the number of tiles**: It calculates how many tiles are needed to cover the entire image based on the image dimensions and tile size.
2. **Download tiles**: It downloads each tile from the constructed URL and saves them locally.
3. **Stitch tiles**: It creates a new image with the correct dimensions and pastes each tile in the correct position.
4. **Save the full image**: The final stitched image is saved in the `high_res_images` directory.

## Example

If the base URL for the tiles is `https://images.eap.bl.uk/EAP262/EAP262_1_2_35_106/1.jp2`, and the image dimensions are 6854x9678 pixels with a tile size of 256x256 pixels, the script will download all necessary tiles and assemble them into the full image.

