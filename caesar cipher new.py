from tkinter import *
from tkinter import ttk

# Function to record each execution in a file named records.txt
def getvals(text, result):
    with open("records.txt","a") as f:
        f.write(f"Operation: Input - {text} - Output - {result}\n")

# Function that contains Caesar Cipher logic
def caesar_cipher(text, shift, decrypt=False):
    result = ""
    if decrypt:
        shift = -shift
    for i in range(len(text)):
        ch = text[i]
        if ch.isalpha():
            shift_amt = shift % 26
            if ch.isupper():
                result += chr((ord(ch) - 65 + shift_amt) % 26 + 65)
            else:
                result += chr((ord(ch) - 97 + shift_amt) % 26 + 97)
        else:
            result += ch
    return result

# Function that encrypts the plain text and displays cipher text as output
def encryption():
    text = pte_entry.get()
    shift = int(shiftenc.get())
    result = caesar_cipher(text, shift, decrypt=False)
    cte.config(state=NORMAL)
    cte.delete(1.0, END)
    cte.insert(END, result)
    cte.config(state=DISABLED)
    getvals(text, result)

# Function that decrypts the cipher text and displays plain text as output
def decryption():
    text = ctd_entry.get()
    shift = int(shiftdec.get())
    result = caesar_cipher(text, shift, decrypt=True)
    ptd.config(state=NORMAL)
    ptd.delete(1.0, END)
    ptd.insert(END, result)
    ptd.config(state=DISABLED)
    getvals(text, result)

# Main window
root = Tk()
root.geometry("800x750")
root.minsize(800,750)
root.maxsize(800,750)
root.title("Caesar Cipher")

# Heading
Label(root, text="Caesar Cipher", font="comicsansms 16 bold underline", pady=15, padx=15).grid(row=1,column=2)

# Plaintext
pte = Label(root, text="Plain Text:", font="arial 10", padx=10)
pte.grid(row=8, column=0)
pte_value = StringVar()
pte_entry = Entry(root, textvariable=pte_value, width=30)
pte_entry.grid(row=8, column=2, pady=(5,5))

# Dropdown menu for shift and encryption button
shiftenc = StringVar()
shiftenc_value= Label(root, text="Shift (1-26):", font="arial 10")
shiftenc_value.grid(row=10, column=0, pady=(0, 5))
shiftenc_dropdown = ttk.Combobox(root, textvariable=shiftenc, width=5)
shiftenc_dropdown['values'] = tuple(str(i) for i in range(1, 27))
shiftenc_dropdown.current(0)
shiftenc_dropdown.grid(row=10, column=1, pady=(0,5))
enc_button = Button(root, text="Encrypt", command=encryption, padx=5, pady=2, bg="lightgray", activebackground="blue",
                   activeforeground="white", cursor="hand2")
enc_button.grid(row=10, column=2, pady=(0,5))

# Ciphertext
cte = Text(root, height=1, width=30, state=DISABLED, fg="red")
cte.grid(row=12, column=2, pady=(0,5))

# Ciphertext as input
ctd = Label(root, text="Cipher Text:", font="arial 10", padx=10)
ctd.grid(row=14, column=0, pady=(20,5))
ctd_value = StringVar()
ctd_entry = Entry(root, textvariable=ctd_value, width=30, fg="red")
ctd_entry.grid(row=14, column=2, pady=(20,5))

# Dropdown menu for shift and decryption button
shiftdec = StringVar()
shiftdec_value = Label(root, text="Shift (1-26):", font="arial 10")
shiftdec_value.grid(row=16, column=0, pady=(0,5))
shiftdec_dropdown = ttk.Combobox(root, textvariable=shiftdec, width=5)
shiftdec_dropdown['values'] = tuple(str(i) for i in range(1, 27))
shiftdec_dropdown.current(0)
shiftdec_dropdown.grid(row=16, column=1, pady=(0,5))
dec_button = Button(root, text="Decrypt", command=decryption, padx=5, pady=2, bg="lightgray", activebackground="blue",
                   activeforeground="white", cursor="hand2")
dec_button.grid(row=16, column=2, pady=(0,5))

# Plaintext
ptd = Text(root, height=1, width=30, state=DISABLED)
ptd.grid(row=18, column=2, pady=(0,5))

# Step-by-step instructions and guidelines to use this software interface and some educational content about this method
# Create a frame to hold additional information
info_frame = Frame(root)
info_frame.grid(columnspan=7)

# Add a label inside this frame for displaying information
info_label = Label(info_frame, text="---------------  A Step-by-Step Guide  ---------------\n\n"
                                    "1. Starting the Application\n"
                                    "Launch the application by clicking on the executable file or shortcut, typically found on your desktop or in your applications folder.\n\n"
                                    "2. Main Interface\n"
                                    "Upon launch, you will see the main interface consisting of several components: an input text box, a dropdown menu for shift selection, buttons for encryption and decryption, and an output text box.\n\n"
                                    "3. Inputting Text\n"
                                    "In the input text box, type or paste the text that you want to encrypt or decrypt. Ensure that the text is properly formatted and free of unwanted characters.\n\n"
                                    "4. Selecting the Shift\n"
                                    "Use the dropdown menu to select the number of positions you wish to shift the letters in your text. This number determines how far each letter will be moved in the alphabet during the encryption or decryption process.\n\n"
                                    "5. Encrypting Text\n"
                                    "Click the 'Encrypt' button after entering your text and selecting your shift. The encrypted text will appear in the output text box, with each letter of your input text shifted by the chosen amount.\n\n"
                                    "6. Decrypting Text\n"
                                    "To decrypt text, enter the encrypted text in the input box, select the original shift used for encryption, and click the 'Decrypt' button. The decrypted text will display in the output text box.\n\n"
                                    "---------------  Educational Information About the Caesar Cipher  ---------------\n\n"
                                    "Modern Applications\n"
                                    "In modern computing, similar techniques evolved into more complex systems like the Vigenère cipher and eventually modern cryptographic algorithms used in data encryption, secure communications, and internet security protocols.\n\n", wraplength=780)
info_label.grid(row=20, column=0, padx=5, pady=5)

# Execution of application
root.mainloop()