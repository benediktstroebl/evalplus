```python
def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotation = 2
    for char in s:
        if char in alphabet:
            index = alphabet.find(char)
            encrypted.append(alphabet[(index + rotation) % len(alphabet)])
        else:
            encrypted.append(char)
    return ''.join(encrypted)
```

This function takes a string **s** as input and iterates through each character. It uses the **'abcdefghijklmnopqrstuvwxyz'** string as the alphabet and rotates each character by multiplying the positional shift by two. The characters not present in the alphabet are appended as is. Finally, the function returns the encrypted string. 

To ensure the function handles edge cases and conforms to the specified behavior, it is recommended to test it with various inputs, such as:
```python
assert encrypt('hi') == 'lm'
assert encrypt('asdfghjkl') == 'ewhjklnop'
assert encrypt('gf') == 'kj'
assert encrypt('et') == 'ix'
``` 
This way, you can confirm that the function works as expected.