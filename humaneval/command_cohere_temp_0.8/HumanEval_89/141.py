```python
def encrypt(s):
    encrypted = []
    for char in s:
        if char.isalpha():
            if char.isupper():
                offset = ord('Z') - ord('A')
                char_code = (ord(char) - ord('A') + 2) % offset * 2 + ord('A')
                encrypted.append(chr(char_code))
            else:
                offset = ord('z') - ord('a')
                char_code = (ord(char) - ord('a') + 2) % offset * 2 + ord('a')
                encrypted.append(chr(char_code))
        else:
            encrypted.append(char)
    return ''.join(encrypted)
```

This code defines the `encrypt` function, which takes a string as input and returns the encrypted string according to the algorithm described in the problem statement. It shifts alphabetic characters by 2 letters down, handling both uppercase and lowercase characters, and leaves non-alphabetic characters unchanged.