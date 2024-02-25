# Image to ASCII Art Converter

This Python script converts images into ASCII art, utilizing the PIL library for image processing and ANSI escape codes for colorizing the output. It offers a flexible way to represent images with text, allowing for customization of the ASCII character used and the scale of the resulting art.

## Features

- **Colorized ASCII Art**: Converts images into ASCII art with colors matching the original image pixels.
- **Customizable Character Representation**: Allows the choice of any character to represent the image pixels in ASCII form.
- **Image Rescaling**: Offers the ability to rescale the image before conversion to control the size of the ASCII output.
- **Error Handling**: Provides clear error messages for common issues, such as incorrect file paths or invalid input parameters.

## Dependencies

- Python 3.x
- Pillow (PIL Fork): Used for image processing tasks.

## Installation

Before running the script, ensure you have Python installed on your system and install the Pillow library using pip:

```sh
pip install Pillow
```

## Usage

The script is designed to be run from the command line with the following syntax:

```sh
python image_to_ascii.py -i <image_path> [-c <character>] [-x <scale_factor>]
```

### Parameters:

- `-i <image_path>`: **Required.** Path to the image file you want to convert.
- `-c <character>`: Optional. The character used for the ASCII art. Defaults to `#`.
- `-x <scale_factor>`: Optional. A float representing the factor by which to scale the image's size before conversion. Defaults to `0.25`.

### Example:

```sh
python image_to_ascii.py -i "/path/to/image.jpg" -c "#" -x 0.25
```

## Functionality

- **`colorize_text(r, g, b, text) -> str`**: Colorizes the provided text using ANSI escape codes based on the specified RGB color.
- **`imageToText(image, character="#") -> str`**: Converts a PIL Image object to a string of ASCII characters.
- **`drawImageAsText(image_path, character="#", x=0.25) -> str`**: Opens an image from the specified path, rescales it, and converts it to ASCII art.

## Terminal Compatibility and Considerations

The script uses ANSI escape codes for colorization, which are supported by many modern terminal emulators. However, compatibility and performance may vary across different terminals and operating systems:

- **Support**: Most Linux, macOS, and Windows 10/11 terminals (through Windows Terminal and PowerShell) support ANSI escape codes. Older terminals or those on earlier versions of Windows may not render colors as expected.
- **Configuration**: Ensure your terminal is configured to process ANSI escape codes and uses a monospaced font for optimal display of ASCII art.
- **Performance**: Large images or high scale factors may result in substantial text output, which could affect rendering performance in some terminals.
- **Color Fidelity**: The script approximates the original image colors in the terminal. The accuracy of these colors can vary depending on the terminal's color scheme and color rendering capabilities.

For the best experience, use a modern terminal emulator with full support for ANSI escape codes and configure your terminal with a suitable monospaced font.

## Error Handling

The script includes error handling for various situations, such as invalid image paths, incorrect parameter types, or unsupported image formats. It ensures a user-friendly experience by providing descriptive error messages.

## Customization

Users can easily customize the ASCII output by changing the character used for conversion or by adjusting the scale factor to achieve the desired level of detail in the ASCII art.

## Conclusion

This script offers a novel way to visualize images through ASCII art, combining the simplicity of text with the complexity of images. It's a versatile tool for creating unique representations of pictures, suitable for use in terminals or text-based media.
