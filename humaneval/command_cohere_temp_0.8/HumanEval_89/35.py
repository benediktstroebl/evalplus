```python
def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in string:
        index = alphabet.find(char)
       if index == -1:
            encrypted += char
        else:
            rotated_index = (index + 2) % 26
            encrypted += alphabet[rotated_index]
    return encrypted
```
This Python script defines a function `encrypt` that takes a string as input and iterates through each character. If the character is not found in the alphabet, it is directly added to the encrypted string. Otherwise, the character's index is calculated relative to the alphabet, rotated by 2, and then appended to the `encrypted` string. This function follows the problem's description, encrypting the input using a shifted alphabet.