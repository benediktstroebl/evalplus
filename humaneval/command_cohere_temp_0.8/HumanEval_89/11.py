```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for char in s:
        # Multiply char by -2 and convert to char
        char_index = alphabet.find(char) - 2
        while char_index < 0:
            char_index += 26
        encrypted.append(alphabet[char_index])
    return ''.join(encrypted)
```

This Python script defines a function `encrypt` taking a string `s` as input and returning an encrypted string using a rotated alphabet scheme. The function iterates through each character in the input string `s`. For each character, it shifts its position in the alphabet downward by 2 and wraps around if needed, then appends the encrypted character to the `encrypted` list. Finally, it joins the encrypted list to produce the encrypted string and returns the result. 

This approach is efficient and maintains a consistent encrypted character mapping, ensuring the ciphertext is readable and easily understood.