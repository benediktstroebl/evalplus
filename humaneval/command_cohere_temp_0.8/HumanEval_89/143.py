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
This function uses a basic modulo operation to rotate the alphabet letters by 2 multiplied by 2 positions down. The rotation is executed within the `modulo` len(alphabet) operation to ensure the rotation wraps around and remains within the bounds of the alphabet. 
The given examples in the prompt return 'lm', 'ewhjklnop', 'kj', and 'ix' respectively.