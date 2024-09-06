```python
def encode(message):
    vowels = 'aeiouAEIOU'
    new_message = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                new_message += chr((char.upper() == char) + 96 - (char in 'AEIOU') * 2 + 97 + (char in 'AEIOU'))
            else:
                new_message += char.swapcase()
        else:
            new_message += char
    return new_message
```