```python
def encrypt(string):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_alphabet = alphabet[2:] + alphabet[:2]

    for char in string:
        if char.isalpha():
            char = char.lower()
            encrypted_index = alphabet.find(char) + 2
            encrypted_char = encrypted_alphabet[encrypted_index]
            encrypted += encrypted_char
        else:
            encrypted += char
    return encrypted
```
This Python script defines a function encrypt(string) that takes a string as input and outputs a string with all alphanumeric characters encrypted using a rotated alphabet map. The script first creates a reference to the English alphabet and then forms a new alphabet with every letter shifted two positions down. Subsequently, each character of the input string is checked, and if it is an alphabetic character, it is encrypted using the rotated alphabet, appended to the encrypted string, and kept non-encrypted otherwise. As a result, the function efficiently encrypts alphanumeric strings using a rotated alphabet map, proving valuable for text encryption tasks.