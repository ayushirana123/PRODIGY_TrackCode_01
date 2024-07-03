import tkinter as tk

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def encrypt_decrypt():
    message = entry_message.get()
    shift = int(entry_shift.get())

    encrypted_message = encrypt(message, shift)
    decrypted_message = decrypt(encrypted_message, shift)

    label_encrypted.config(text="Encrypted message: " + encrypted_message)
    label_decrypted.config(text="Decrypted message: " + decrypted_message)

# Create GUI window
window = tk.Tk()
window.title("Caesar Cipher")

# Message entry
label_message = tk.Label(window, text="Enter message:")
label_message.grid(row=0, column=0)
entry_message = tk.Entry(window)
entry_message.grid(row=0, column=1)

# Shift entry
label_shift = tk.Label(window, text="Enter shift value:")
label_shift.grid(row=1, column=0)
entry_shift = tk.Entry(window)
entry_shift.grid(row=1, column=1)

# Encrypt/Decrypt button
button_encrypt_decrypt = tk.Button(window, text="Encrypt/Decrypt", command=encrypt_decrypt)
button_encrypt_decrypt.grid(row=2, columnspan=2)

# Encrypted message label
label_encrypted = tk.Label(window, text="")
label_encrypted.grid(row=3, columnspan=2)

# Decrypted message label
label_decrypted = tk.Label(window, text="")
label_decrypted.grid(row=4, columnspan=2)

window.mainloop()
