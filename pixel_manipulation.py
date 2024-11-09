from PIL import Image
import random
import os

def encrypt_image(image_path, output_path):
    """
    Encrypts the image by shuffling its pixels randomly.
    """
    if not os.path.exists(image_path):
        print(f"Error: The file '{image_path}' does not exist.")
        print(f"Trying to open: {image_path}")
        return

    try:
        # Open and convert the image to RGB format
        image = Image.open(image_path).convert("RGB")
        pixels = list(image.getdata())
        
        # Generate a list of shuffled indices
        width, height = image.size
        total_pixels = width * height
        indices = list(range(total_pixels))
        random.shuffle(indices)
        
        # Create a new list of pixels according to the shuffled indices
        shuffled_pixels = [pixels[i] for i in indices]
        
        # Save the encrypted image
        encrypted_image = Image.new("RGB", image.size)
        encrypted_image.putdata(shuffled_pixels)
        encrypted_image.save(output_path)
        print(f"Encrypted image saved to {output_path}")
        
        # Save shuffled indices to a file
        with open("shuffled_indices.txt", "w") as file:
            file.write(" ".join(map(str, indices)))
                
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def decrypt_image(image_path, output_path):
    """
    Decrypts the image by restoring the original pixel positions.
    """
    if not os.path.exists(image_path):
        print(f"Error: The file '{image_path}' does not exist.")
        return

    if not os.path.exists("shuffled_indices.txt"):
        print("Error: The shuffled indices file 'shuffled_indices.txt' is missing.")
        return

    try:
        # Read the shuffled indices
        with open("shuffled_indices.txt", "r") as file:
            indices = list(map(int, file.read().strip().split()))
        
        # Open the encrypted image and get pixels
        image = Image.open(image_path).convert("RGB")
        pixels = list(image.getdata())
        
        # Create a list to hold decrypted pixels
        decrypted_pixels = [None] * len(pixels)
        
        # Reverse the shuffle using indices to restore the original order
        for i, index in enumerate(indices):
            decrypted_pixels[index] = pixels[i]
        
        # Save the decrypted image
        decrypted_image = Image.new("RGB", image.size)
        decrypted_image.putdata(decrypted_pixels)
        decrypted_image.save(output_path)
        print(f"Decrypted image saved to {output_path}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    print("Image Encryption and Decryption Tool")
    print("1. Encrypt an Image")
    print("2. Decrypt an Image")
    choice = input("Enter your choice (1 or 2): ")

    if choice not in ["1", "2"]:
        print("Invalid choice. Please select 1 or 2.")
        return
    
    image_path = input("Enter the path of the image: ")
    output_path = input("Enter the output path for the processed image: ")

    if choice == "1":
        encrypt_image(image_path, output_path)
        
    elif choice == "2":
        decrypt_image(image_path, output_path)

if __name__ == "__main__":
    main()
