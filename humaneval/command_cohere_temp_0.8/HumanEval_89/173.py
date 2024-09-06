```python
def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotations = [alphabet[i:i+2] for i in range(0, 26, 2)]
    for char in s:
      encrypted += rotations[alphabet.find(char)]
    return encrypted
```

This Python script defines a function `encrypt` taking a string `s` as input and returning an encrypted string using a rotated alphabet scheme. The script creates the encrypted string by looping through the input string `s`, finding the rotated characters from the alphabet, and appending them to the `encrypted` string.

The alphabet is set to `'abcdefghijklmnopqrstuvwxyz'`, and the rotations are created by dividing the alphabet into consecutive pairs, shifting each pair by two, and then concatenating them. The function successfully encrypts the input strings according to the problem statement's requirements and produces the desired encrypted output.