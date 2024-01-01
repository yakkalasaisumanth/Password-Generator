from tkinter import *
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import os
import base64
from tkinter import messagebox

root =Tk()
root.title("DECRYPTOR")
root.configure(bg = "sky blue")

def exit():
	root.destroy()

def decrypt():

	filename = "authentication.txt.enc"

	def file_exists(filename):
		return os.path.isfile(filename)

	def derive_key(password, salt):
		kdf = PBKDF2HMAC(
			algorithm=hashes.SHA256(),
			length=32,
			salt=salt,
			iterations=100000,
			backend=default_backend()
			)
		key = kdf.derive(password.encode())
		return base64.urlsafe_b64encode(key)

	def decrypt_file(filename, password):
		with open(filename, 'rb') as file:
			data = file.read()

		salt = data[:16]
		encrypted_data = data[16:]

		key = derive_key(password, salt)
		cipher_suite = Fernet(key)

		decrypted_data = cipher_suite.decrypt(encrypted_data)
		original_file = filename[:-4]
		with open(original_file, 'wb') as file:
			file.write(decrypted_data)

		configfile = Text(root, wrap=WORD, width=45, height= 20)
		configfile.grid(row = 4, column=0, columnspan=2)

		with open("authentication.txt", "r") as f:
			configfile.insert(INSERT, f.read())

		messagebox.showinfo("Info", "Data Has Been Decrypted Sucessfully." +"\n" + "Please Open .txt File In The Current Directory.")
	if file_exists(filename):
		
		password = password_entry.get()
		decrypt_file(filename, password)
		os.remove("authentication.txt")
	else:
		messagebox.showinfo("Info", "Please Open password Genarator First.")


	return



welcome_label = Label(root, text = "Welcome To DECRYPTOR.", fg = "green", font = "poppins")
welcome_label.grid(row = 0, column=0, columnspan =2)
password_label = Label(root, text= "Please Enter The Password You Used To Encrypt The File.", fg = "green", font = "poppins")
password_label.grid(row =1, column= 0, pady=10, padx =10, sticky ="w")

password_entry = Entry(root, width=20, borderwidth=6, show ="*")
password_entry.grid(row = 1, column=1, sticky ="s")

button_1 = Button(root, text ="DECRYPT", command = decrypt, padx= 40, pady =20, bg ="yellow", fg = "black")
button_1.grid(row = 2, column=0, columnspan =2, pady =10)
button_1 = Button(root, text ="EXIT", command = exit, padx= 40, pady =20, bg ="yellow", fg = "black")
button_1.grid(row = 3, column=0, columnspan =2, pady =10)



root.mainloop()

