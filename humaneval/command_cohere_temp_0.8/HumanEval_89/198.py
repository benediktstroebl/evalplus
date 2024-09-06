```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in s:
        index = alphabet.find(char)
        encrypted += alphabet[index + 2 * 2:] + alphabet[index:index + 2]
    return encrypted
```

This Python script defines a function `encrypt` taking a string as an argument and returning an encrypted string. The algorithm uses a two-step process:
1. Encrypt the first character to the second character of the alphabet, shifting by 2 places.
2. Encrypt the second character using the first character of the alphabet, then shift the alphabet back by 2 places.

The script goes through each character in the input string `s` and iterates through the `alphabet`. It finds the index of the current character and then constructs the encrypted character using the two-step process explained above. The `encrypted` string is then returned.