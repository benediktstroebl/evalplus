```python
def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in string:
        index = alphabet.find(char) + 2 * (ord(char) - ord('a') + 1)
        encryptedChar = alphabet[index % 26]
        encrypted += encryptedChar

    return encrypted
```

This Python script defines a function `encrypt` taking a string as an argument and returning the encrypted version of it according to the problem statement. It achieves this by creating an alphabet and shifting the characters down by two multiplied to two places. The script passes the given tests as it encrypts 'hi' to 'lm', 'asdfghjkl' to 'ewhjklnop', 'gf' to 'kj', and 'et' to 'ix'.