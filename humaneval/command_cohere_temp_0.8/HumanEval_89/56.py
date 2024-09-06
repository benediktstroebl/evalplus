```python
def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in string:
        index = alphabet.find(char)
       encrypted += alphabet[index+2]*2
```
The code uses a simple algorithm to encrypt a string by shifting the alphabet clockwise by two letters twice for each character.  It begins by setting the alphabet as a string consisting of all lowercase letters. The variable `encrypted` is initialized as an empty string to store the encrypted message. 

The algorithm uses a for loop to iterate through each character in the string. It implants the `find()` method to each character to obtain its index in the alphabet. It then supplements the index with 2 and twice to move the alphabet clockwise. The outcome is concatenated to the `encrypted` string. Ultimately, the function returns the `encrypted` string, concluding the process.  This approach enables users to encrypt messages using the specified rotation of the alphabet.