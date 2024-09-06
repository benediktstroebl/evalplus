```python
def encode(message):
    vowels = 'aeiouAEIOU'
    new_message = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                new_message += chr((97 + (ord(char) - 96 - i)) % 26 + 96)
            else:
                new_message += chr(ord(char) ^ 32)
        else:
            new_message += char
    return new_message
```