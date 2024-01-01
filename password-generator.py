from tkinter import *
import os
import hashlib
import secrets
from more_itertools import random_permutation
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from tkinter import messagebox
import string
import random
import os
import base64


root =Tk()
root.title("PASWWORD GENERATOR")
root.configure(bg="#ddfff7")






def EXIT():
	root.destroy()

def newwindow(Signup):
	newwindow = Toplevel(root)
	newwindow.title("SIGNUP")
	newwindow.configure(bg="#ddfff7")


	filename = "credentials.txt"


	def Signup():

		username = a.get()
		password = b.get()

		def write_credentials(filename, username, password):
			with open(filename, "w") as file:
				file.write(username + "\n")
				salt = secrets.token_hex(16)

				password += salt

				password_hash = hashlib.sha256(password.encode()).hexdigest()

				file.write(salt + '\n')

				file.write(password_hash + '\n')

		filename = "credentials.txt"

		write_credentials(filename, username, password)

		


		newwindow.destroy()

	def Mainmenu():
		newwindow.destroy()



	welcome_label = Label(newwindow, text = "This is your first time using this program.", fg = "green", font = "poppins", bg = "#ddfff7")
	welcome_label.grid(row = 0, column=0, columnspan=2)
	welcome_label_1 = Label(newwindow, text ="Please Create your username and password.", fg = "green", font = "poppins", bg ="#ddfff7")
	welcome_label_1.grid(row = 1, column=0, columnspan=2)

	a = Entry(newwindow, width = 20, borderwidth = 4)
	a.grid(row = 2, column = 1)
	a.focus_set()
	b = Entry(newwindow, show ="*", width = 20, borderwidth = 4)
	b.grid(row = 3, column = 1)
	b.focus_set()
	a_label = Label(newwindow, text = "username", fg = "#006BBB", font= "poppins", bg = "#ddfff7")
	a_label.grid(row=2, column=0)
	b_label = Label(newwindow, text = "password", fg = "#006BBB", font= "poppins", bg = "#ddfff7")
	b_label.grid(row =3 , column = 0)



	button_1 = Button(newwindow, text = "Signup", command = Signup, padx = 40, pady=20, bg = "#FFC872", fg = "black")
	button_1.grid(row=4, column = 0, columnspan = 2)
	button_2 = Button(newwindow, text = "Mainmenu", command = Mainmenu, padx = 40, pady=20, bg = "#FFC872", fg = "black")
	button_2.grid(row=5, column = 0, columnspan = 2)

def newwindow_1(Login):

	def disable_clsoe():
		messagebox.showinfo("Close","Close Button Is Disabled." + "\n" + "Please Use Exit Button.")


	newwindow_1 = Toplevel(root)
	newwindow_1.title("LOGIN")
	newwindow_1.configure(bg = "#ddfff7")
	newwindow_1.protocol("WM_DELETE_WINDOW", disable_clsoe)

	def Login():

		username = c.get()
		password = d.get()
		filename = "credentials.txt"

		def read_credentials(filename):
			with open(filename , "r") as file:
				username = file.readline().strip()
				salt = file.readline().strip()
				password_hash = file.readline().strip()
			return username, salt, password_hash
		def validate_credentials(username, password, correct_username, correct_salt, correct_hash):
			if username == correct_username:
				password += correct_salt
				password_hash = hashlib.sha256(password.encode()).hexdigest()
				if password_hash == correct_hash:
					return True
			return False

		correct_username, correct_salt, correct_hash = read_credentials(filename)

		valid = validate_credentials(username, password, correct_username, correct_salt, correct_hash)

		if valid:
			
			newwindow_1.destroy()
			root.destroy()

			newwindow_4=Tk()
			newwindow_4.title("PASSWORD GENERATOR")
			newwindow_4.configure(bg= "#88F4FF")


			def Close_window():
				messagebox.showinfo("Close", "Close Button Is Disabled." + "\n" + "Please Use Exit Button.")

			newwindow_4.protocol("WM_DELETE_WINDOW", Close_window)

			filename = "authentication.txt"

			def exit():
				newwindow_4.destroy()

			def Encrypt():
				user_password = user_password_entry.get()

				def derive_key(user_password, salt):
					kdf = PBKDF2HMAC(
						algorithm=hashes.SHA256(),
						length=32,
						salt=salt,
						iterations=100000,
						backend=default_backend()
					)
					key = kdf.derive(user_password.encode())
					return base64.urlsafe_b64encode(key)

				def encrypt_file(filename, user_password):
					salt = os.urandom(16)
					key = derive_key(user_password, salt)
					cipher_suite = Fernet(key)

					with open(filename, "rb") as file:
						plaintext = file.read()

					encrypted_data = cipher_suite.encrypt(plaintext)

					encrypt_file_name = filename + '.enc'

					with open(encrypt_file_name, "wb") as file:
						file.write(salt + encrypted_data)
					messagebox.showinfo("Info", "File Encrypted and Saved In The Current Directory")

				encrypt_file(filename, user_password)
				os.remove("authentication.txt")

			def submit():
				capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
				small_letteres = "abcdefghijklmnopqrstuvwxyz"
				numbers = "1234567890"
				special_characters = "`~!@#$%^&*()-_=+*:;[],.<>?/'"

				if cap.get() > 8:
					messagebox.showinfo("Info", "Please Enter Capital letters Between 0-8")
				elif small.get() >8:
					messagebox.showinfo("Info", "Please Enter small letters Between 0-8")
				elif num.get() >8:
					messagebox.showinfo("Info", "Please Enter Numbers Between 0-8")
				elif spec.get() >8:
					messagebox.showinfo("Info", "Please Enter special characters Between 0-8")
				elif cap.get() >8 or small.get() >8 or num.get() >8 or spec.get() >8:
					messagebox.showinfo("Info", "Please Enter Numbers Between 0-8")
				else:
					cap_letters = random.choices(capital_letters, k = cap.get())
					sm_letters = random.choices(small_letteres, k= small.get())
					digits = random.choices(numbers, k = num.get())
					characters = random.choices(special_characters, k = spec.get())
					string_pass = str(cap_letters + sm_letters + digits + characters)
					passwd = string_pass.replace(" ", "").replace( ',', '').replace( '[', '').replace( ']', '').replace("'", "")
					half_passwd = str(random_permutation(passwd))
					_passwd = half_passwd.replace(" ", "").replace( ',', '').replace( '[', '').replace( ']', '').replace("'", "")
					final_passwd = _passwd
					
					
					username = username_entry.get()
					password = final_passwd

					def file_exists(filename):
						return os.path.isfile(filename)

					def Write_capability(filename, username, password):
						with open(filename, "w") as f:
							f.write("username: " + username + "\n")
							f.write("password: " + password + "\n")

					global filename
					filename = "authentication.txt"

					if file_exists(filename):
						with open(filename, "a") as f:
							f.write("username: " + username + "\n")
							f.write("password: " + password + "\n")
					else:
						Write_capability(filename, username, password)

					username_entry.delete(0, END)
					caps.delete(0, END)
					smalls.delete(0, END)
					nums.delete(0, END)
					specials.delete(0, END)
					messagebox.showinfo("Info", "Username & Password Sucessfully Saved To Authentication.txt" + "\n" + "\n" + "To Create Another Username & Password Please Fill The Details Again and Click Submit" + "\n" + "\n" +Please Encrypt The File By Entering The password and click Encrypt.")

				return
			

			welcome_label = Label(newwindow_4, text = "WELCOME TO PASSWORD GENERATOR", font = "poppins", fg= "#625AD8", bg ="#88F4FF")
			welcome_label.grid(row = 0 , column=0, columnspan = 2)

			cap = IntVar()
			small = IntVar()
			num = IntVar()
			spec = IntVar()

			username_entry = Entry(newwindow_4,  width = 40 , borderwidth=4)
			username_entry.grid(row = 1, column=1, ipadx =10, pady=10, sticky = 'S')
			username_entry.focus_set()
			caps = Entry(newwindow_4, textvariable = cap, width = 40, borderwidth =4)
			caps.grid(row = 2, column =1, pady=10, sticky="s")
			smalls = Entry(newwindow_4, textvariable =small,width = 40, borderwidth = 4)
			smalls.grid(row = 3, column = 1, pady =10, sticky="s")
			nums = Entry(newwindow_4,textvariable = num, width = 40, borderwidth =4)
			nums.grid(row = 4, column = 1, pady=10, sticky="s")
			specials = Entry(newwindow_4,textvariable = spec, width = 40, borderwidth=4)
			specials.grid(row =5, column = 1, pady=10, sticky="s")
			user_password_entry = Entry(newwindow_4, show = "*" , width = 40, borderwidth=4)
			user_password_entry.grid(row =8, column = 1, pady=10, sticky="s")

			username_label = Label(newwindow_4, text = "Enter username or email",fg= "#625AD8", bg ="#88F4FF", font = "poppins")
			username_label.grid(row=1, column=0, sticky = "w")
			caps_label = Label(newwindow_4, text = "Please Enter Number Of Capital Letters(0-8)", font = "poppins", fg= "#625AD8", bg ="#88F4FF")
			caps_label.grid(row =2, column=0, sticky = "w")
			smalls_label = Label(newwindow_4, text = "Please Enter Number Of Small Letters(0-8)", font = "poppins", fg= "#625AD8", bg ="#88F4FF")
			smalls_label.grid(row =3, column=0, sticky = "w")
			nums_label = Label(newwindow_4, text = "Please Enter Number Of  Digits(0-8)", font = "poppins", fg= "#625AD8", bg ="#88F4FF")
			nums_label.grid(row =4, column=0, sticky = "w")
			specials_label = Label(newwindow_4, text = "Please Enter Number Of special Characters(0-8)", font = "poppins", fg= "#625AD8", bg ="#88F4FF")
			specials_label.grid(row =5, column=0, sticky = "w")

			encrypt_label = Label(newwindow_4, text= "Please Enter a Password To encrypt The File", fg= "#625AD8", bg ="#88F4FF", font="poppins")
			encrypt_label.grid(row = 7, column =0, columnspan = 2)
			user_password_label = Label(newwindow_4, text = "Please Enter a Password for Encrypting The File", font = "poppins", fg= "#625AD8", bg ="#88F4FF")
			user_password_label.grid(row =8, column=0, sticky = "w")

			button_1 = Button(newwindow_4, text = "SUBMIT", command = submit, bg = "#1F9CE4", fg ="black", padx = 40, pady = 20)
			button_1.grid(row = 6, column = 0, columnspan = 2, pady=10)
			button_3 =Button(newwindow_4, text= "ENCRYPT", command =Encrypt, bg ="#1F9CE4", fg = "black", padx=40, pady=20)
			button_3.grid(row = 9, column = 0, columnspan=2, pady=10)
			button_2 = Button(newwindow_4, text = "EXIT", command = exit, bg = "#1F9CE4", fg ="black", padx = 40, pady = 20)
			button_2.grid(row = 10, column = 0, columnspan = 2, pady=10)

			newwindow_4.mainloop()
		else:
			messagebox.showinfo("Info", "Invalid Username Or Password Entered!.")
	
	def EXIT():
		newwindow_1.destroy()

	welcome_label = Label(newwindow_1, text = "Please Login Into Your Account", bg = "#ddfff7", fg = "green", font = "poppins")
	welcome_label.grid(row = 0, column = 0)

	c = Entry(newwindow_1, width = 20, borderwidth=4 )
	c.grid(row=1, column=1,)
	c.focus_set()
	d = Entry(newwindow_1, show = "*", width = 20, borderwidth=4 )
	d.grid(row=2, column=1,)
	d.focus_set()

	c_label = Label(newwindow_1, text = "username", fg ="#006BBB", bg ="#ddfff7", font = "poppins")
	c_label.grid(row = 1, column=0)
	d_label = Label(newwindow_1, text = "password", fg ="#006BBB", bg ="#ddfff7", font = "poppins")
	d_label.grid(row = 2, column=0)


	button_1 = Button(newwindow_1,text = "Login", command = Login, padx=40, pady=20, fg = "black", bg = "#FFC872")
	button_1.grid(row = 3, column= 0, columnspan=2)
	button_2 = Button(newwindow_1, text = "exit" ,command = EXIT, padx=40, pady=20, fg = "black", bg = "#FFC872")
	button_2.grid(row = 4, column= 0, columnspan=2)

welcome_label = Label(root, text = "WELCOME TO PASSWORD GENERATOR.", fg = "green", font ="poppins", bg = "#ddfff7")
welcome_label.grid(row = 0, column = 0, columnspan = 2)

button_1 = Button(root, text="Signup", command = lambda:newwindow("Signup"), padx = 58, pady = 20, bg = '#ffa69e', fg = 'black', borderwidth =4)
button_1.grid(row=1, column=0)
button_2 =Button(root, text="Login", command = lambda:newwindow_1("Login"), padx = 58, pady = 20, bg = '#ffa69e', fg = 'black', borderwidth =4)
button_2.grid(row=1, column=1)
button_3 =Button(root, text="EXIT", command = EXIT, padx = 58, pady = 20, bg = '#ffa69e', fg = 'black', borderwidth =4)
button_3.grid(row=2, column=0, columnspan=2)

end_label =Label(root, text = "CREATED BY", fg = "green", font = "poppins", bg = "#ddfff7")
end_label.grid(row = 3, column = 0, columnspan=2)
end_label_1 =Label(root, text = "Y SAI SUMANTH", fg = "green", font = "poppins", bg ="#ddfff7")
end_label_1.grid(row = 4, column = 0, columnspan=2)


root.mainloop()
