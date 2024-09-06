```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in s:
        offset = ord(char) + 2 * (ord(char) // 2)
        encryptedChar = chr(offset % 26 + 97)
        encrypted += encryptedChar
    return encrypted
```

This Python script defines a function `encrypt` taking a string `s` as input and returning an encrypted string using a shifted alphabet. To encrypt a letter, it first creates an offset by adding two to the ASCII value of the character, then incrementing that offset by two for each additional character since the last encryption (this is the 'multiplied by two places' aspect). This large offset is then wrapped around the alphabet by taking the modulus 26 to ensure the resulting character remains within the bounds of the alphabet. The encrypted character is then added to the evolving encrypted string, which is returned once all letters are processed.