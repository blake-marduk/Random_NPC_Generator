import tkinter as tk
from tkinter import filedialog, messagebox, PhotoImage
from PIL import Image, ImageDraw, ImageFont
import os
import sys

# --- 1. Your Existing Standard Galactic Alphabet Mapping ---
# IMPORTANT: Replace this with your actual SGA translation logic/dictionary.
# This is a simplified placeholder. Ensure your translation output is valid
# Unicode for the SGA characters.
SGA_MAPPING = {
        'A': '\uEB40', 'B': '\uEB41', 'C': '\uEB42', 'D': '\uEB43',
        'E': '\uEB44', 'F': '\uEB45', 'G': '\uEB46', 'H': '\uEB47',
        'I': '\uEB48', 'J': '\uEB49', 'K': '\uEB4A', 'L': '\uEB4B',
        'M': '\uEB4C', 'N': '\uEB4D', 'O': '\uEB4E', 'P': '\uEB4F',
        'Q': '\uEB50', 'R': '\uEB51', 'S': '\uEB52', 'T': '\uEB53',
        'U': '\uEB54', 'V': '\uEB55', 'W': '\uEB56', 'X': '\uEB57',
        'Y': '\uEB58', 'Z': '\uEB59',
        '"': '\uEB5A', "'": '\uEB5B', '.': '\uEB5C'
}

def translate_to_sga(text):
    """
    Translates English text to Standard Galactic Alphabet using the SGA_MAPPING.
    """
    translated_chars = [SGA_MAPPING.get(char, char) for char in text]
    return "".join(translated_chars)

# --- 2. Font Handling for Packaged App (from previous response) ---
def get_font_path(font_filename="standard-galactic-alphabet-unpixelated.ttf"):
    """
    Determines the correct path to the font file, whether running as a script
    or a PyInstaller-bundled executable.
    """
    if getattr(sys, 'frozen', False):
        # The script is running as a bundled executable (e.g., with PyInstaller)
        base_path = sys._MEIPASS
    else:
        # The script is running normally (e.g., from Python interpreter)
        base_path = os.path.abspath(os.path.dirname(__file__))

    return os.path.join(base_path, "fonts", font_filename)

# --- 3. Image Generation Function ---
def generate_sga_image(sga_text, font_path, font_size=30, padding=20):
    """
    Generates an image of the Standard Galactic Alphabet text.
    Returns a PIL Image object.
    """
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        messagebox.showerror("Font Error", f"Could not load font from: {font_path}\n"
                                           "Please ensure 'standard-galactic-alphabet-unpixelated.ttf' is in the 'fonts' folder.")
        return None

    # Calculate text size using the font
    # getbbox returns (left, top, right, bottom)
    bbox = font.getbbox(sga_text)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Add padding around the text
    image_width = text_width + 2 * padding
    image_height = text_height + 2 * padding

    # Create a new image with white background
    img = Image.new('RGB', (max(image_width, 100), max(image_height, 50)), color=(255, 255, 255))
    d = ImageDraw.Draw(img)

    # Draw the text (adjust position for padding)
    d.text((padding, padding), sga_text, font=font, fill=(0, 0, 0)) # Black text

    return img

# --- 4. GUI Application ---
class SGATranslatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Standard Galactic Alphabet Translator")
        master.geometry("600x450") # Set a default window size
        master.resizable(False, False) # Make window non-resizable

        # Try to load a small placeholder image for initial display
        # This part is optional but makes the GUI look nicer if you have an icon
        try:
            icon_path = os.path.join(os.path.dirname(__file__), "sga_icon.png")
            # Replace with a small, 64x64 or 128x128 pixel transparent PNG
            # if you want an icon in the GUI window itself.
            # Otherwise, comment out the next two lines.
            # self.icon_image = PhotoImage(file=icon_path)
            # master.iconphoto(True, self.icon_image)
        except Exception:
            pass # No icon found, continue without it

        self.font_path = get_font_path("SGA1.ttf")

        # Input Frame
        self.input_frame = tk.Frame(master, padx=10, pady=10)
        self.input_frame.pack(fill=tk.X)

        self.label = tk.Label(self.input_frame, text="Enter your message (English):", font=('Arial', 12))
        self.label.pack(anchor=tk.W)

        self.text_input = tk.Text(self.input_frame, height=5, width=60, wrap=tk.WORD, font=('Arial', 12))
        self.text_input.pack(pady=5)

        self.translate_button = tk.Button(self.input_frame, text="Translate & Generate Image", command=self.process_message, font=('Arial', 12, 'bold'))
        self.translate_button.pack(pady=10)

        # Image Display Frame (Optional, for quick preview)
        # For larger images, just opening the file is better.
        self.image_display_frame = tk.Frame(master, padx=10, pady=10, bd=2, relief=tk.GROOVE)
        self.image_display_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        self.image_label = tk.Label(self.image_display_frame, text="Generated SGA Image will appear here (or open in viewer)...", font=('Arial', 10), wraplength=400)
        self.image_label.pack(pady=20)


    def process_message(self):
        english_message = self.text_input.get("1.0", tk.END).strip()

        if not english_message:
            messagebox.showwarning("Input Error", "Please enter a message to translate.")
            return

        sga_translated_message = translate_to_sga(english_message)

        # Generate the image
        img = generate_sga_image(sga_translated_message, self.font_path)

        if img:
            # Ask user where to save the image
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
                title="Save Standard Galactic Alphabet Image As"
            )
            if file_path:
                try:
                    img.save(file_path)
                    messagebox.showinfo("Success", f"Image saved successfully to:\n{file_path}\n\n"
                                                   "Opening image now...")
                    # Open the image using the default system viewer
                    os.startfile(file_path) # For Windows
                    # For macOS: os.system(f'open "{file_path}"')
                    # For Linux: os.system(f'xdg-open "{file_path}"')
                except Exception as e:
                    messagebox.showerror("Save Error", f"Failed to save image: {e}")
            else:
                messagebox.showinfo("Cancelled", "Image saving cancelled.")
        else:
            # Error message already displayed by generate_sga_image
            pass

# --- Main Application Execution ---
if __name__ == "__main__":
    root = tk.Tk()
    app = SGATranslatorApp(root)
    root.mainloop()