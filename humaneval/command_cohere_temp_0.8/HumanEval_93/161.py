```python
def encode(message):
    vowels = 'AEIOUaeiou'
    new_message = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                new_message += chr((char.lower() - 97) + (ord(vowels[vowels.index(char)])-96))
            else:
                new_message += chr(97+((char.lower() - 97) + (1 if char.isupper() else -1)))
        else:
            new_message += char
    return new_message
```