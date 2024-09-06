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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encoded = ''
    for char in s:
        index = alphabet.find(char)
        encoded += alphabet[index + 2*2:] + alphabet[index:index+2]
    return encoded
```

The `encrypt` function takes a string `s` as input and iterates through each character in the string. It uses the `find` method to convert each character into its index in the alphabet and then uses the rotated alphabet to encode the character, adding it to the `encoded` string. The encoded string is then returned as the encrypted result.