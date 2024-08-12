from PIL import Image
import pillow_heif
import config


def convert_heic_to_jpeg(heic_file_path: str, output_file_path: str):
    # Open the HEIC file
    heif_file = pillow_heif.read_heif(heic_file_path)

    # Convert to a PIL Image
    image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data)

    # Save the image as JPEG
    image.save(output_file_path, format="JPEG")
    print(f"Image saved as {output_file_path}")


if __name__ == "__main__":
    # Example usage:
    convert_heic_to_jpeg(
        heic_file_path=f"{config.IMAGES_DIR}/IMG_6931.HEIC",
        output_file_path=f"{config.IMAGES_DIR}/dogs.jpg"
    )
