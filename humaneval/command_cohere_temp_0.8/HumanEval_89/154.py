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

This encrypt function first determines whether the character is alphabetical, then decides whether to rotate the character depending on whether the difference between the character's ASCII code and 96 (the ASCII code for 'a') is divisible by 16, and then rotates the character by that many characters. It returns the encrypted message as a string. You can test this function by calling it with different input strings and comparing the output with the examples provided in the problem statement.