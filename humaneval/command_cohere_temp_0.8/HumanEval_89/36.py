```python
def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in s:
        if char.isalpha():
            offset = (alphabet.find(char) + 2) % 26
            encryptedChar = alphabet[offset:][:offset]
            encrypted = encrypted + encryptedChar
        else:
            encrypted = encrypted + char
    return encrypted
```
This Python script defines a function encrypt(s) that processes an input string s as specified in the problem. It iterates through each character in the input string s. If the character is an alphabet letter, it calculates an offset by finding the character's index in the alphabet and then adding 2 (modulo 26 to wrap around). This offset determines the new position in the alphabet. It then constructs the encrypted character by extracting a letter from the shifted position in the alphabet. The encrypted character is then appended to the encrypted string. If the character isn't an alphabet letter, it's directly appended to the encrypted string without any alteration. Finally, the function returns the encrypted string.