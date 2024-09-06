```python
def encode(message):
    vowels = 'AEIOUaeiou'
    new_message = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                new_message += chr(97 + (ord(char) - 96 + 2) % 26)
            else:
                new_message += chr(ord(char) ^ 32)
        else:
            new_message += char
    return new_message
```