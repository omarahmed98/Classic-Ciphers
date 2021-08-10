import tkinter as tk
from orderedset import OrderedSet
import numpy as np
import string
import random
import numpy as np
import egcd  

alphabet = "abcdefghijklmnopqrstuvwxyz"

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

FONT = ("calbri", 20, "bold")
FONT2 = ("Arial", 10, "bold")

def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext.upper():
        if char.isalpha():
            ciphertext += chr((ord(char) + key - 65) % 26 + 65)
        else:
            ciphertext += char
    return ciphertext
class Playfair:
    def __init__(self, passphrase='', skip_char='J', skip_char_replacement='I', pad_char='X'):
        self.char_set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.passphrase = passphrase.upper()
        self.skip_char = skip_char
        self.skip_char_replacement = skip_char_replacement
        self.pad_char = pad_char
        self.grid_map = {}
        self.grid_map_rev = {}
        self.build_grid()

    def build_grid(self):
        """ Builds the encoding/decoding grid based on passphrase and skip_letter """
        passphrase_list = list(OrderedSet(self.passphrase))
        ordered_char_set = passphrase_list + list(OrderedSet(self.char_set) - OrderedSet(self.passphrase + self.skip_char))

        grid_width = 5
        grid_col = 0
        grid_row = 0
        self.grid_map = {}
        for c in ordered_char_set:
            self.grid_map[c] = (grid_col, grid_row)
            grid_col = grid_col + 1
            if grid_col == grid_width:
                grid_col = 0
                grid_row = grid_row + 1
        self.grid_map_rev = dict([(value, key) for key, value in self.grid_map.items()])

        return self.grid_map, self.grid_map_rev

    # helpers
    def get_char_pos(self, c):
        return self.grid_map[c]

    def get_char(self, c, r):
        return self.grid_map_rev[(c % 5, r % 5)]

    #
    def process(self, message):
        """ Encrypt using the Playfair cipher """
        message = message.upper().replace(' ', '').replace(self.skip_char, self.skip_char_replacement)
        message = message.upper().replace('\n', '').replace(self.skip_char, self.skip_char_replacement)
        if len(message) % 2 != 0:
            message = message + self.pad_char
        message = list(message)
        i = 0
        output = []
        while len(message) > 0:
            a = message.pop(0)
            b = message.pop(0)

            movement = 1
            if a == b:  # if the digram is repeating letters then convert the latter to replacement
                b = self.pad_char

            c1, r1 = self.get_char_pos(str(a))
            c2, r2 = self.get_char_pos(str(b))
            if r1 == r2:
                output.append(self.get_char(c1 + movement, r1))
                output.append(self.get_char(c2 + movement, r1))
            elif c1 == c2:
                output.append(self.get_char(c1, r1 + movement))
                output.append(self.get_char(c1, r2 + movement))
            else:  # box case
                output.append(self.get_char(c2, r1))
                output.append(self.get_char(c1, r2))

        return ''.join(output)
def Hill(message,key,dim):
    dimension = dim  # Your N
    # Generate the alphabet
    alphabet = string.ascii_uppercase
    # Encrypted message
    encryptedMessage = ""
    # Group message in vectors and generate crypted message
    for index, i in enumerate(message):
        values = []
        # Make bloc of N values
        if index % dimension == 0:
            for j in range(0, dimension):
                if(index + j < len(message)):
                    values.append([alphabet.index(message[index + j])])
                else:
                    values.append([random.randint(0,25)])
            # Generate vectors and work with them
            vector = np.matrix(values)
            vector = key * vector
            vector %= 26
            for j in range(0, dimension):
                encryptedMessage += alphabet[vector.item(j)]

    # Show the result
    return encryptedMessage

def gen_Key_Vignere(string, key,mode):
    key = list(key)
    if len(string) == len(key):
        return(key)
    elif mode == "rep":
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    elif mode == "auto":
        for i in range(len(string) -
                       len(key)):
            key.append(string[i % len(string)])
    return("" . join(key))
def Vignere(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))
def vernamEncryption(plaintext, key):
    mappingsDict = {}
    alphabets = "abcdefghijklmnopqrstuvwxyz".upper()
    for alphabet in alphabets:
        mappingsDict[alphabet] = ord(alphabet) - 65
    # Initializing ciphertext
    ciphertext = ''

    for i in range(len(plaintext)):
        ptLetter = plaintext[i]
        keyLetter = key[i]
        # Performing vernam encryption step
        sum = mappingsDict[ptLetter] + mappingsDict[keyLetter]
        # Subtracting 26 if sum overflows above values
        if sum >= 26:
            sum -= 26
        # Adding to ciphertext
        ciphertext += chr(sum + 65)

    # Returning ciphertext
    return ciphertext

class ClassicCipherGUI:
    def __init__(self, master):
        master.title("Classic Cipher GUI")
        self.ciphertext = tk.StringVar(master, value="")
        self.mode = tk.BooleanVar(master)
        self.key = tk.IntVar(master)
        self.key1 = tk.StringVar(master)
        self.key22 = tk.StringVar(master)
        self.key2 = tk.StringVar(master)
        self.key3 = tk.StringVar(master)
        self.key4 = tk.StringVar(master)
        # Encryption controls
        self.encrypt_button1 = tk.Button(master, text="Encrypt CAESAR", command=lambda: self.encrypt_callback1(), font=FONT).grid(row=3, column=2)
        self.encrypt_button2 = tk.Button(master, text="Encrypt PLAY", command=lambda: self.encrypt_callback2(master), font=FONT).grid(row=4, column=2)
        self.key_label = tk.Label(master, text="Instert matrix row by row and put one space between every element", fg = "blue", font=FONT2).grid(row=8, column=1)
        self.key_label = tk.Label(master, text="Instert matrix row by row and put one space between every element", fg = "blue",
                                  font=FONT2).grid(row=9, column=1)
        self.encrypt_button3 = tk.Button(master, text="Encrypt HILL 2*2", command=lambda: self.encrypt_callback31(), font=FONT).grid(row=8, column=2)
        self.encrypt_button3 = tk.Button(master, text="Encrypt HILL 3*3", command=lambda: self.encrypt_callback3(), font=FONT).grid(row=9, column=2)

        self.encrypt_button4 = tk.Button(master, text="Encrypt VIGNERE", command=lambda: self.encrypt_callback4(), font=FONT).grid(row=10, column=2)
        self.encrypt_button5 = tk.Button(master, text="Encrypt VERNAM", command=lambda: self.encrypt_callback5(), font=FONT).grid(row=12, column=2)


        # Key controls
        self.key_label = tk.Label(master, text="(Choose mode for vigenere 0 or 1) auto = 0 / repeat = 1 ", fg = "red",
                                  font=FONT2).grid(row=10, column=1, padx = 250,sticky=tk.W)
        self.key_entry = tk.Entry(master, textvariable=self.mode, width=10, font=FONT2).grid(row=11, column=1, sticky=tk.W, padx=350)

        self.key_label = tk.Label(master, text="Key of CAESAR", font=FONT).grid(row=3, column=0)
        self.key_entry = tk.Entry(master, textvariable=self.key, width=10, font=FONT).grid(row=3, column=1, sticky=tk.W, padx=20)

        self.key_label1 = tk.Label(master, text="Key of play", font=FONT).grid(row=4, column=0)
        self.key_entry1 = tk.Entry(master, textvariable=self.key1, width=10, font=FONT).grid(row=4, column=1, sticky=tk.W, padx=20)

        self.key_label1 = tk.Label(master, text="Key of HILL 2*2", font=FONT).grid(row=8, column=0)
        self.key_entry1 = tk.Entry(master, textvariable=self.key22, width=10, font=FONT).grid(row=8, column=1, sticky=tk.W, padx=20)

        self.key_label1 = tk.Label(master, text="Key of HILL 3*3", font=FONT).grid(row=9, column=0)
        self.key_entry1 = tk.Entry(master, textvariable=self.key2, width=10, font=FONT).grid(row=9, column=1, sticky=tk.W, padx=20)

        self.key_label1 = tk.Label(master, text="Key of Vigenere", font=FONT).grid(row=10, column=0)
        self.key_entry1 = tk.Entry(master, textvariable=self.key3, width=10, font=FONT).grid(row=10, column=1, sticky=tk.W, padx=20)

        self.key_label1 = tk.Label(master, text="Key of Vernam", font=FONT).grid(row=12, column=0)
        self.key_entry1 = tk.Entry(master, textvariable=self.key4, width=10, font=FONT).grid(row=12, column=1, sticky=tk.W, padx=20)
        # Key controls

        # Ciphertext controls
        self.cipher_label = tk.Label(master, text="Last example Ciphertext", fg="red", font=FONT2).grid(row=0, column=0)
        self.cipher_entry = tk.Entry(master, textvariable=self.ciphertext, width=50, font=FONT)
        self.cipher_entry.grid(row=0, column=1, padx=20)


    def get_mode(self):
        try:
            key_val = self.mode.get()
            return key_val
        except tk.TclError:
            pass
    def get_key(self):
        try:
            key_val = self.key.get()
            return key_val
        except tk.TclError:
            pass
    def get_key1(self):
        try:
            key_val = self.key1.get()
            return key_val
        except tk.TclError:
            pass
    def get_key22(self):
        try:
            key_val = self.key22.get()
            return key_val
        except tk.TclError:
            pass
    def get_key2(self):
        try:
            key_val = self.key2.get()
            return key_val
        except tk.TclError:
            pass
    def get_key3(self):
        try:
            key_val = self.key3.get()
            return key_val
        except tk.TclError:
            pass
    def get_key4(self):
        try:
            key_val = self.key4.get()
            return key_val
        except tk.TclError:
            pass



   # call back

    def encrypt_callback1(self):
        key = self.get_key()
        with open("caesar_plain.txt", "r") as a_file:
            for line in a_file:
                stripped_line = line.strip()
                ciphertext = encrypt(stripped_line, key)
                self.cipher_entry.delete(0, tk.END)
                self.cipher_entry.insert(0, ciphertext)
                file = open('caesar_plain_out.txt', 'a+')
                file.write(ciphertext + '\n')
                file.close()
    def encrypt_callback2(self,master):

        key = self.get_key1()
        with open("playfair_plain.txt", "r") as a_file:
            for line in a_file:
                stripped_line = line.strip()
                stripped_line = stripped_line[:-1]
                play = Playfair(passphrase= key, skip_char='J', skip_char_replacement='I', pad_char='X')
                ciphertext = play.process(stripped_line)
                self.cipher_entry.delete(0, tk.END)
                self.cipher_entry.insert(0, ciphertext)
                file = open('playfair_plain_out.txt', 'a+')
                file.write(ciphertext + '\n')
                file.close()

    def encrypt_callback3(self):
        #K = np.matrix([[3, 3], [2, 5]])
        key = self.get_key2()
        a_list = key.split()
        map_object = map(int, a_list)
        l = list(map_object)
        right_key = np.matrix([[l[0],l[1],l[2]], [l[3],l[4],l[5]], [l[6],l[7],l[8]]])
        with open("hill_plain_3x3.txt", "r") as a_file:
            for line in a_file:
                stripped_line = line.strip().upper()
                ciphertext = Hill(stripped_line, right_key,3)
                self.cipher_entry.delete(0, tk.END)
                self.cipher_entry.insert(0, ciphertext)
                file = open('hill_plain_3x3_out.txt', 'a+')
                file.write(ciphertext + '\n')
                file.close()
    def encrypt_callback31(self):
        key = self.get_key22()
        a_list = key.split()
        map_object = map(int, a_list)
        l = list(map_object)
        right_key = np.matrix([[l[0],l[1]], [l[2],l[3]]])
        with open("hill_plain_2x2.txt", "r") as a_file:
            for line in a_file:
                stripped_line = line.strip().upper()
                ciphertext = Hill(stripped_line, right_key,2)
                self.cipher_entry.delete(0, tk.END)
                self.cipher_entry.insert(0, ciphertext)
                file = open('hill_plain_2x2_out.txt', 'a+')
                file.write(ciphertext + '\n')
                file.close()
    def encrypt_callback4(self):
        key = self.get_key3()
        with open("vigenere_plain.txt", "r") as a_file:
            for line in a_file:
                stripped_line = line.strip().upper()
                #stripped_line = stripped_line[:-1]
                modee = self.get_mode()
                mode = ""
                if (modee == 1):
                    mode = "rep"
                elif (modee == 0):
                    mode = "auto"
                if(len(stripped_line)==len(key)):
                    new_key = key.upper()
                else:
                    new_key = gen_Key_Vignere(stripped_line,key,mode).upper()
                ciphertext = vernamEncryption(stripped_line, new_key)
                self.cipher_entry.delete(0, tk.END)
                self.cipher_entry.insert(0, ciphertext)
                file = open('vigenere_plain_out.txt', 'a+')
                file.write(ciphertext + '\n')
                file.close()
    def encrypt_callback5(self):
        key = self.get_key4().upper()
        with open("vernam_plain.txt", "r") as a_file:
            for line in a_file:
                stripped_line = line.strip().upper()
                # stripped_line = stripped_line[:-1]
                if(len(stripped_line)==len(key)):
                    ciphertext = vernamEncryption(stripped_line, key)
                    self.cipher_entry.delete(0, tk.END)
                    self.cipher_entry.insert(0, ciphertext)
                    file = open('vernam_plain_out.txt', 'a+')
                    file.write(ciphertext + '\n')
                    file.close()
                else:
                    ciphertext = "Error KEY not equal length MESSAGE"
                    self.cipher_entry.delete(0, tk.END)
                    self.cipher_entry.insert(0, ciphertext)
                    file = open('vernam_plain_out.txt', 'a+')
                    file.write(ciphertext + '\n')
                    file.close()





if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1400x800+120+120")
    caesar = ClassicCipherGUI(root)
    root.mainloop()

