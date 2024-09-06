```python
def encode(message):
    vowels = 'AEIOUaeiou'
    new_message = ''.join(
        c.swapcase() if c not in vowels else vowels.index(c) + 2 + vowels[vowels.index(c) + 1]
        for c in message
    )
    return new_message
```

This script defines a function `encode` that takes a message as an input. It iterates through each character in the message and makes the following changes:
1. It swaps the case of all non-vowel characters, ensuring that all letters are in uppercase or lowercase.
2. It replaces all vowel characters with a character that is two places ahead of them in the English alphabet. For example, "A" is replaced with "C", "E" is replaced with "G", and so on. 

The resulting string is then returned as the encoded message. 

The script aims to provide a whimsical and unique way of encoding messages, making them more challenging to decipher without knowing the key mechanism.