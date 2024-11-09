from PIL import Image  # Importing the Image module from PIL (Pillow) for image processing
import random  # Importing random module to shuffle pixels
import os  # Importing os module to handle file paths and existence checks

def encrypt_image(image_path, output_path):
    """
    Encrypts the image by shuffling its pixels randomly.
    """
    # Check if the image file exists at the given path
    if not os.path.exists(image_path):
        print(f"Error: The file '{image_path}' does not exist.")
        print(f"Trying to open: {image_path}")
        return  # Exit if file does not exist

    try:
        # Open the image and convert it to RGB format (3 channels for Red, Green, and Blue)
        image = Image.open(image_path).convert("RGB")
        # Extract all the pixel values from the image
        pixels = list(image.getdata())
        
        # Get the width and height of the image
        width, height = image.size
        total_pixels = width * height  # Total number of pixels in the image
        
        # Create a list of indices (from 0 to total_pixels - 1)
        indices = list(range(total_pixels))
        random.shuffle(indices)  # Shuffle the indices randomly
        
        # Create a new list of pixels according to the shuffled indices
        shuffled_pixels = [pixels[i] for i in indices]
        
        # Create a new image and set the shuffled pixels
        encrypted_image = Image.new("RGB", image.size)
        encrypted_image.putdata(shuffled_pixels)
        # Save the encrypted image to the specified output path
        encrypted_image.save(output_path)
        print(f"Encrypted image saved to {output_path}")
        
        # Save the shuffled indices to a text file for later decryption
        with open("shuffled_indices.txt", "w") as file:
            file.write(" ".join(map(str, indices)))
                
    except Exception as e:
        # Handle any exceptions that may occur during the process
        print(f"An unexpected error occurred: {e}")

def decrypt_image(image_path, output_path):
    """
    Decrypts the image by restoring the original pixel positions.
    """
    # Check if the encrypted image file exists
    if not os.path.exists(image_path):
        print(f"Error: The file '{image_path}' does not exist.")
        return  # Exit if file does not exist

    # Check if the shuffled indices file exists
    if not os.path.exists("shuffled_indices.txt"):
        print("Error: The shuffled indices file 'shuffled_indices.txt' is missing.")
        return  # Exit if the indices file does not exist

    try:
        # Read the shuffled indices from the file
        with open("shuffled_indices.txt", "r") as file:
            indices = list(map(int, file.read().strip().split()))
        
        # Open the encrypted image and convert it to RGB
        image = Image.open(image_path).convert("RGB")
        # Extract all the pixel values from the image
        pixels = list(image.getdata())
        
        # Create a list to hold the decrypted pixels
        decrypted_pixels = [None] * len(pixels)
        
        # Reverse the shuffle using the saved indices to restore the original order
        for i, index in enumerate(indices):
            decrypted_pixels[index] = pixels[i]
        
        # Create a new image and set the decrypted pixels
        decrypted_image = Image.new("RGB", image.size)
        decrypted_image.putdata(decrypted_pixels)
        # Save the decrypted image to the specified output path
        decrypted_image.save(output_path)
        print(f"Decrypted image saved to {output_path}")
        
    except Exception as e:
        # Handle any exceptions that may occur during the process
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to interact with the user for choosing encryption or decryption.
    """
    print("Image Encryption and Decryption Tool")
    print("1. Encrypt an Image")
    print("2. Decrypt an Image")
    # Ask the user to choose either encryption or decryption
    choice = input("Enter your choice (1 or 2): ")

    if choice not in ["1", "2"]:
        print("Invalid choice. Please select 1 or 2.")
        return  # Exit if the user input is not valid
    
    # Get the file paths for the image and the output
    image_path = input("Enter the path of the image: ")
    output_path = input("Enter the output path for the processed image: ")

    if choice == "1":
        # If the user chose encryption, call the encrypt function
        encrypt_image(image_path, output_path)
        
    elif choice == "2":
        # If the user chose decryption, call the decrypt function
        decrypt_image(image_path, output_path)

if __name__ == "__main__":
    main()  # Run the main function to start the program
