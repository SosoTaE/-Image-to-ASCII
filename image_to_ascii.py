# built in
import sys

# installed
from PIL import Image

def colorize_text(r: int, g: int, b: int, text: str) -> str:
    """
    Colorizes the provided text with the specified RGB color using ANSI escape codes.

    Parameters:
        r (int): The red component of the RGB color.
        g (int): The green component of the RGB color.
        b (int): The blue component of the RGB color.
        text (str): The text to be colorized.

    Returns:
        str: The colorized text as a string with ANSI escape codes for the specified RGB color.
    """
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def imageToText(image: Image.Image, character: str = "#") -> str:
    """
    Converts a PIL Image object to a string of ASCII characters, with each pixel's color represented by the specified character.

    Parameters:
        image (Image.Image): The image to convert to ASCII art.
        character (str, optional): The character to use for the ASCII art representation. Defaults to "#".

    Returns:
        str: A string representation of the image in ASCII art.

    Raises:
        TypeError: If `image` is not an instance of `Image.Image`.
        ValueError: If `character` is not a single character.
    """
    if not isinstance(image, Image.Image):
        raise TypeError(f"image should be type of {Image.Image}")

    if len(character) != 1:
        raise ValueError("Character length should be 1")

    text = ""

    for i in range(image.height):
        for j in range(image.width):
            rgb = image.getpixel((j, i))
            text += colorize_text(*rgb, text=character)

        text += "\n"

    return text

def drawImageAsText(image_path: str, character: str = "#", x: float = 0.25) -> str:
    """
    Opens an image from the specified path, rescales it, and converts it to ASCII art using the specified character.

    Parameters:
        image_path (str): The path to the image file.
        character (str, optional): The character to use for the ASCII art. Defaults to "#".
        x (float, optional): The factor by which to scale the image's size. Defaults to 2.

    Returns:
        str: The ASCII art representation of the image.

    Raises:
        ValueError: If `character` is not a single character or if `x` cannot be converted to a float.
    """
    if len(character) != 1:
        raise ValueError("Character length should be 1")

    if isinstance(x, str):
        try:
            x = float(x)
        except ValueError:
            raise ValueError("-x value should be a number")

    image = Image.open(image_path).convert("RGB")
    size = (int(image.width * x), int(image.height * x))
    image = image.resize(size=size)

    text = imageToText(image, character)

    return text


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("No arguments were passed.")

    definitions = {
        "-i": "image_path",
        "-c": "character",
        "-x": "x"
    }

    params = dict()

    keys = sys.argv[1::2]
    values = sys.argv[2::2]
    for key, value in zip(keys, values):
        if key not in definitions:
            print(f"Key {key} is not recognized")

        params[definitions[key]] = value

    try:
        text = drawImageAsText(**params)
        print(text)
    except Exception as e:
        print(str(e))
