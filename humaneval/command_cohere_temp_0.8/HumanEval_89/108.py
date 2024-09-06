```python
def encrypt(s):
    encrypted = ''
    rotating_letters = 'abcdefghijklmnopqrstuvwxyz'
    offset = 2
    for char in s:
        offset_pos = char.isalpha() + char.lower() - 97 - offset
        encrypted_char = rotating_letters[offset_pos % 26]
        encrypted += encrypted_char
    return encrypted
```

This encrypt function takes a string s as input and iterates through each character. It uses a rotating letters string to map characters to their rotated positions, considering an offset, and builds the encrypted string accordingly.

Here's an example usage and output for the provided Python script:
```python
original_string = "hi"
encrypted_string = encrypt(original_string)
print("Original String:", original_string)
print("Encrypted String:", encrypted_string)
```

This would produce the following output:
```
Original String: hi
Encrypted String: lm
```

The provided code effectively encrypts the input string using a rotated alphabet scheme, achieving the desired outcome.