# PRODIGY_CS_02
Python-based Image Encryption and Decryption Tool that allows users to encrypt and decrypt images by manipulating pixel positions.

# Description
This project implements a simple image encryption and decryption tool using pixel manipulation. It encrypts an image by randomly shuffling its pixels, and it can decrypt the image by restoring the original pixel order. This tool demonstrates basic cryptography principles applied to images, providing a hands-on approach to learning about encryption algorithms and image processing.

# Features
1. Encrypts an image by randomly shuffling its pixels to create a scrambled version of the image.
2. Restores the original image by reversing the shuffle using a list of shuffled pixel indices stored in a separate file.
3. Utilizes pixel-level manipulation (shuffling of pixels) to create the encryption effect.
4. Saves the encrypted image in a specified output path.
5. Saves the shuffled pixel indices in a file (shuffled_indices.txt), which is used for decrypting the image later.
6. Command-line interface allowing users to choose between encrypting or decrypting an image with simple inputs.
7. Works with images in various formats such as .jpg, .jpeg, .png, and others supported by the Pillow library.
8. The tool can be used on any system that supports Python and Pillow, including Windows, macOS, and Linux.
9. Includes error handling for common issues like missing files or incorrect file paths.
10. The project is open-source, allowing users to modify or contribute to the code.

# Requirements
To run this tool, you need to have the following installed:

Python 3.x
Pillow library (for image processing) - install using the command " pip install pillow "

# How It Works
When you run the program, you will be prompted to choose between encrypting or decrypting an image. 

The steps depend on your choice:

1. Encrypting an Image:
    The program will ask you for the path to the image you want to encrypt and the desired output path for the encrypted image.

    It will randomly shuffle the pixels of the image and save the result to the specified output path.

    The shuffled pixel indices are saved to a file (shuffled_indices.txt) to enable decryption later.

2. Decrypting an Image:
    The program will ask you for the path to the encrypted image and the output path for the decrypted image.
    It will read the shuffled pixel indices from the shuffled_indices.txt file.
    The pixels are rearranged based on these indices to restore the image to its original state.
    The decrypted image is saved to the specified output path.

# Error Handling:

If the file path to the image does not exist, or if the shuffled_indices.txt file is missing during decryption, the program will print an error message.

# Example
Running the Program:

1. Encrypting an Image:
    Choose option 1 (Encrypt an Image).
    Enter the path to the image you want to encrypt (e.g., path/to/image.jpg).
    Enter the output path for the encrypted image (e.g., path/to/encrypted_image.jpg).

2. Decrypting an Image:
    Choose option 2 (Decrypt an Image).
    Enter the path to the encrypted image (e.g., path/to/encrypted_image.jpg).
    Enter the output path for the decrypted image (e.g., path/to/decrypted_image.jpg).


