```python
def encode(message):
    vowels = 'aeiouAEIOU'
    new_message = ''.join(
        c.swapcase() if c.isalpha() and c not in vowels else
        vowels.index(c) + 2 for c in message if c.isalpha()
    )
    return new_message
```

This script defines a function `encode(message)`, which takes an input message. It iterates through each character in the input message. For alphabetic characters, it checks if the character is a vowel. If it is, it replaces the vowel with the character two places ahead of its alphabetical position (e.g., 'a' becomes 'c', 'e' becomes 'g', and so on). For non-vowel characters, it simply swaps the case. Finally, it returns the modified message.