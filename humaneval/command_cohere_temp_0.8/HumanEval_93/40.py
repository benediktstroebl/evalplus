```python
def encode(message):
    vowels = 'AEIOUaeiou'
    new_message = ''
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                new_message += chr((char.lower() in vowels) * 2 + (vowels.index(char.lower()) + 1) % 2  + vowels[vowels.index(char.lower())])
            else:
                new_message += char
        else:
            new_message += char
    return new_message
```