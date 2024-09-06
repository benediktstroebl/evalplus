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
            char = chr(ord(char) - 2 * ((ord(char) - 96) % 16))
        encrypted = encrypted + char
    return encrypted
```

This Python script defines a function encrypt(s) that takes a string s as input and encrypts it using a rotated alphabet scheme. The algorithm works by subtracting 2 * ((ord(char) - 96) % 16) from the ASCII value of each letter character in the string, where 96 is the ASCII value of the letter 'a'. The expression (ord(char) - 96) % 16 calculates a cyclical difference and the modulus value is used to prevent negative values and limit the rotation to a specific range. After encryption, the result is a string containing the encrypted characters.