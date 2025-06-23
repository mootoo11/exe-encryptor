import os
import base64
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file():
    input_path = input_entry.get()
    output_path = output_entry.get()
    custom_key = key_entry.get().strip()

    if not input_path or not output_path:
        messagebox.showerror("Error", "Please select both input and output files.")
        return

    # Use provided key or generate a new one
    if custom_key:
        try:
            key = custom_key.encode()
            Fernet(key)  # Validate key
        except Exception:
            messagebox.showerror("Invalid Key", "Provided key is not a valid Fernet key.")
            return
    else:
        key = generate_key()

    cipher = Fernet(key)

    try:
        with open(input_path, 'rb') as file:
            original = file.read()

        encrypted = cipher.encrypt(original)

        with open(output_path, 'wb') as enc_file:
            enc_file.write(encrypted)

        # Generate decryption stub
        encrypted_filename = os.path.basename(output_path)
        stub_code = f"""
import os
import subprocess
import tempfile
from cryptography.fernet import Fernet

key = b'{key.decode()}'
cipher = Fernet(key)

def decrypt_and_run():
    encrypted_file = '{encrypted_filename}'
    try:
        with open(encrypted_file, 'rb') as enc_file:
            encrypted = enc_file.read()
        decrypted = cipher.decrypt(encrypted)
        temp_dir = tempfile.gettempdir()
        decrypted_file = os.path.join(temp_dir, 'input.exe')
        with open(decrypted_file, 'wb') as dec_file:
            dec_file.write(decrypted)
        subprocess.run([decrypted_file], check=True)
        os.remove(decrypted_file)
    except Exception as e:
        print(f"[!] Error: {{e}}")

if __name__ == "__main__":
    decrypt_and_run()
"""

        # Save stub in same directory as output
        stub_path = os.path.join(os.path.dirname(output_path), "decrypt_stub.py")
        with open(stub_path, "w") as stub_file:
            stub_file.write(stub_code)

        result_label.config(text=f"✅ Encryption completed!\n🔑 Key:\n{key.decode()}\n📄 Stub saved to:\n{stub_path}")

    except Exception as e:
        messagebox.showerror("Encryption Error", f"Something went wrong:\n{e}")

# GUI Setup
root = tk.Tk()
root.title("EXE Encryptor GUI")

tk.Label(root, text="Input EXE File:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1)
tk.Button(root, text="Browse", command=lambda: input_entry.insert(0, filedialog.askopenfilename(filetypes=[("EXE files", "*.exe")]))).grid(row=0, column=2)

tk.Label(root, text="Output DLL File:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1)
tk.Button(root, text="Browse", command=lambda: output_entry.insert(0, filedialog.asksaveasfilename(defaultextension=".dll"))).grid(row=1, column=2)

tk.Label(root, text="Optional Key (Base64):").grid(row=2, column=0, sticky="e", padx=5, pady=5)
key_entry = tk.Entry(root, width=50)
key_entry.grid(row=2, column=1, columnspan=2)

tk.Button(root, text="Encrypt and Generate Stub", command=encrypt_file, bg="#4CAF50", fg="white").grid(row=3, column=1, pady=15)

result_label = tk.Label(root, text="", fg="green", justify="left")
result_label.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()
