import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import qrcode

class QRCodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("400x400")

        # Create a label and entry for QR code data
        self.label = tk.Label(root, text="Enter data for QR Code:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=5)
        
        # Create a button to generate QR code
        self.generate_button = tk.Button(root, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack(pady=10)
        
        # Create a label to display the QR code image
        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)
        
        # Create a button to save the QR code
        self.save_button = tk.Button(root, text="Save QR Code", command=self.save_qr_code)
        self.save_button.pack(pady=10)
        
        self.qr_image = None

    def generate_qr_code(self):
        data = self.entry.get()
        if not data:
            messagebox.showwarning("Input Error", "Please enter data for QR code.")
            return
        
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        # Create an image from the QR code
        img = qr.make_image(fill='black', back_color='white')
        
        # Convert the image to a format Tkinter can use
        self.qr_image = ImageTk.PhotoImage(img)
        
        # Update the label to show the QR code
        self.image_label.config(image=self.qr_image)

    def save_qr_code(self):
        if self.qr_image is None:
            messagebox.showwarning("Save Error", "No QR code generated to save.")
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", ".png"), ("All files", ".*")]
        )
        if file_path:
            # Save the image
            img = qr.make_image(fill='black', back_color='white')
            img.save(file_path)
            messagebox.showinfo("Save Successful", f"QR code saved to {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGenerator(root)
    root.mainloop()