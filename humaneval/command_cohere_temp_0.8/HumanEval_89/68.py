```python
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    encrypted = ''
    for char in s:
        if char.isalpha():
            char = chr(ord(char) - 2 * (ord(char) // 2))
        encrypted = encrypted + char
    return encrypted
```

This Python script defines a function `encrypt()` using a for loop to iterate through each character in the input string `s`. For alphabetic characters, it performs a bit of arithmetic to determine the correct rotated character and concatenates it to the evolving `encrypted` string. It returns the encrypted string. This solves the problem's requirement to encrypt a string with the alphabet rotated in a specified manner.