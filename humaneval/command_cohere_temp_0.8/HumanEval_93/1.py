```python
def encode(message):
    vowels = 'aeiouAEIOU'
    new_message = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                new_message += chr((char.lower() in vowels) + (ord(char.upper()) - 96) + 2)
            else:
                new_message += char.swapcase()
        else:
            new_message += char
    return new_message
```