```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for char in s:
        index = alphabet.find(char)
       encrypted.append(alphabet[(index + 2 * 2) % 26])
    encrypted = ''.join(encrypted)
    return encrypted
```
This Python script defines a function `encrypt` taking a string s as an argument and returning an encrypted version of the string. Within the function, it initializes an alphabet spanning 'abcdefghijklmnopqrstuvwxyz' and later, it loops through each character char in the provided input string s. For each character, it finds its position within the alphabet, and then applies a roll-over-2-letters-at-a-time scheme to determine the encrypted character. Afterward, it joins the encrypted characters together into a single string and returns the encrypted string. 

Here's an example usage of the function for a variety time:
```python
print(encrypt('hi')) # lm
print(encrypt('asdfghjkl')) # ewhjklnop
print(encrypt('gf')) # kj
print(encrypt('et')) # ix
```
This function fulfills the desired behavior outlined in the prompt, leveraging Python's string manipulation and modular arithmetic capabilities.  While this encryption approach is straightforward, it constitutes a basic example of encrypting messages using a caesar cipher.