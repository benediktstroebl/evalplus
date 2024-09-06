```python
def encode(message):
    vowels = 'aeiouAEIOU'
    new_message = ''.join(
        c.swapcase() if c not in vowels else vowels.index(c) + 2 + vowels[vowels.index(c) + 1]
        for c in message
    )
    return new_message
```

This script defines a function `encode` that takes a message as an input. It iterates over each character in the message and does the following:
1. Makes all characters uppercase if they are lowercase or vice versa. This is done using the `swapcase` method.
2. If the character is a vowel, it is replaced by the character that is two places ahead of it in the alphabet. This is achieved by calculating the index of the vowel in the string `vowels` and then adding 2. The next vowel is then picked and the process is repeated.

The script assumes that the input contains only letters.