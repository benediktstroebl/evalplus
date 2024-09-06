```python
def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shift = 2
    for char in s:
        if char.isalpha():
            offset = ord(char) - 96 + shift
            encrypted.append(chr(offset + 96))
        else:
            encrypted.append(char)
    return ''.join(encrypted)
```

This function takes a string **s** as input and returns a string encrypted with the rotated alphabet. It shifts each letter down by **2** multiplied to **2** positions. The function only shifts the letters of the alphabet, leaving non-alphabet characters unchanged. To maintain the alphabet's rotation, it continuously shifts each letter by a constant offset, ensuring the encryption is consistent.