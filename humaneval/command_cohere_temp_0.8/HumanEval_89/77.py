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
    encrypted = ''
    for char in s:
        index = alphabet.find(char)
        new_index = (index + 2 * 2) % len(alphabet)
        encrypted += alphabet[new_index]
    return encrypted
``` 

This code snippet defines the `encrypt` function, which takes a string as input and iterates through each character in the input string. It uses the `find` method to determine the index of each character in the alphabet, adjusts the index by multiplying `2` by `2` and then wrapping the index modulo the length of the alphabet, and then appends the character from the new index in the alphabet to the `encrypted` string. Finally, the `encrypted` string is returned as the output. 

Here is an example usage of the code: 
```python
print(encrypt('hi')) # lm
print(encrypt('asdfghjkl')) # ewhjklnop
print(encrypt('gf')) # kj
print(encrypt('et')) # ix
``` 

The example outputs show the encrypted text resulting from inputting various string types.