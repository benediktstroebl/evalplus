```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for char in s:
        index = alphabet.find(char)
       new_index = (index + 2 * 2) % len(alphabet)
        encrypted.append(alphabet[new_index])
    return ''.join(encrypted)
```
This function uses a basic Caesar cipher encryption where the alphabet letters are shifted by a predetermined number of places. In this case, the alphabet is shifted down by two multiplied by two places. This ensures the alphabet rotates correctly and wraps around to the beginning if needed. This function accepts any string as input and returns the encrypted version of the string. 

Here is an example function call:
```python
encrypt('hi') # returns 'lm'
```
Here is another example function call:
```python
encrypt('asdfghjkl') # returns 'ewhjklnop'
```
And here is the last example function call:
```python
encrypt('gf') # returns 'kj'
```
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
    encrypted = []
    for char in s:
        index = alphabet.find(char)
        new_index = (index + 2 * 2) % len(alphabet)
        encrypted.append(alphabet[new_index])
    return ''.join(encrypted)
```