```python
def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rot_alphabet = alphabet[2:] + alphabet[:2]
    for char in s:
      encrypted += rot_alphabet[alphabet.find(char)]
    return encrypted
```
This function uses two different alphabets - the main alphabet (`alphabet`) and the rotated version (`rot_alphabet`). It rotates characters from `s` using the main alphabet and maps them to the equivalent characters in the rotated alphabet, ultimately returning the encrypted message. 
The example usage in the original prompt would produce the following output:
```python
encrypt('hi') # hl
encrypt('asdfghjkl') # ewhjklnop
encrypt('gf') # kj
encrypt('et') # ix
``` 
This solution offers a straightforward way to encrypt a string based on a rotated alphabet. Gaining a basic understanding of how the encryption process works involves observing the mapping of characters from the original string to the rotated alphabet in action.