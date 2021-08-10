# Classic-Ciphers

This application includes classical ciphers with user-interface implemented by tkinter and python.

# Requirments

to make the application work properly, you should make text files for the input text in the same directory of the executable file or the main code.
name of files created to be like I uploaded.
you could change the input in the text files with the code.
Finally, the application would put the results in output file like the name of input file but extra "output" included.

# Contents

code of the classical ciphers in main.py and executable file.

# User-interface 

![image](https://user-images.githubusercontent.com/22713770/128878922-2e1e33b7-05bf-40fa-ac34-826f04ab2ef1.png)

# Details

My application consists of five ciphers encoding algorithms with GUI via Tkinter, to  make it easy to use this library with only user interface!
Ciphers Implemented: -
1-	Caesar Cipher
2-	Play Fair Cipher
3-	Hill Cipher
4-	Vigenere Cipher
5-	Vernam Cipher
Part one: (Coding)
Every algorithms consists of plaintext and key, the type of the differ from one algorithm to another.
In Caser >> integer ,,,  Play Fair>> string ,,, Hill >> matrix of integers,,,
Vigenere Cipher >> string ,,, Vernam Cipher >> string.
Taking the input from file and printing the output to file, so when coding the design was as follow:
-	First, I wrote the Function or Class (like play fair as I need the initialization of grid for every sample) for encryption.
-	Then, I wrote  the backbone class “ClassicCipherGUI”, in this class I initialized the key type for every algorithm first in __init__ and initialized the buttons which make events after clicking it.
-	Every button call a function (callback() ) which is responsible of reading the plain text from the file then calling the algorithm function or class , finally print the output in file.
-	Next to main button there are key buttons which consist of label of the key and the entry to take the value from the user in the GUI.
-	Get_key function made to get the value from the entry of the key and then pass the key to function callback() which is doing encryption as I said before.
-	Get_mode function to get the mode of the Vigenere algorithm which 0 “equal” auto and 1 equal “repeating”.
-	Finally, the main function which I call the program through it.
Part Two: (GUI)
-	The GUI is easy to use, and friendly as to use every algorithm all you want to put input file with main.exe (caesar_plain.txt - hill_plain_2x2.txt - hill_plain_3x3.txt - playfair_plain.txt - vernam_plain.txt - vigenere_plain.txt) and then put the key in the entry of the algorithm needed to encrypted.
-	Then press the button of Encrypt …….. like “ ENCRYPT CAESAR”, the output will be printed in file and the last example of the output will be shown at “last example Cipher text example”.
-	In case of writing the array of the Hill 2*2 or 3*3 , insert digits row by row and one space between every digit as I wrote in the GUI interface with blue color.
-	In case of using Vigenere, there is a button to choose the mode of the process, and the default value is auto “which means when the length of key is smaller than plain then uses first characters of plain in key” if you typed “1” then “ I will repeat the characters of the key to be the same length of plain text”.
