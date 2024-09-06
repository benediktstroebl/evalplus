```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in s:
        offset = ord(char) + 2 * (ord(char) // 2)
        encryptedchar = chr(offset % 26 + 97)
        encrypted += encryptedchar
    return encrypted
```

This function defines an alphabet to be used for the encryption, and then loops through the provided string `s`. Within the loop, it calculates an offset for each character by adding 2 * (ord(char) // 2) to the ASCII value of the character, and then performs a modulo operation to ensure the offset wraps around the alphabet. It then appends the character that is calculated from the offset to the `encrypted` string. 

The code block provided will successfully encrypt any string using the specified encryption technique. While this kind of encryption is relatively straightforward to break, it serves well to illustrate more complex encryption algorithms. 

This solution should be compatible with Python 3.x. If you are using a different version, minor adjustments may be required.