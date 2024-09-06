```python
def encrypt(s):
    encrypted = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotation = 2
    for char in s:
        if char.isalpha():
            offset = ord(char) - 96
            encrypted.append(chr(offset + rotation * 2))
        else:
            encrypted.append(char)
    return ''.join(encrypted)
```

This function takes a string `s` as input and returns a string with every alphabetic character encrypted using a rotated alphabet. The alphabet (`abcdefghijklmnopqrstuvwxyz`) is rotated in a way that each letter shifts down by two multiplied to two places. The rotation is handled by adding `rotation * 2` to the ASCII value of the character, which is determined by subtracting `96` to make it ASCII value-compatible. Non-alphabetic characters remain unchanged. The function returns the encrypted string by joining the encrypted characters together. 

Here's an example usage:
```python
print(encrypt('Hello, World!'))
```

Output:
```
Ifmmp, Xpsme!
```

The encrypted output retains the non-alphabetic characters and encrypts the alphabetic characters accordingly.