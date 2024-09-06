```python
def encode(message):
    vowels = 'aeiouAEIOU'
    swapped = ''.join(char.swapcase() if char.isalpha() else char for char in message)
    return swapped.lower() if char.lower() not in vowels else chr(ord(swapped.lower()) + 2) for char in swapped
```

This script defines a function `encode` that takes a message as an input. It sequentially executes two transformations:
1. To each character of the message, it applies a case swap if the character is alphabetic (using the `swapcase()` method), or leaves the character unchanged if it's not. These transformations are applied sequentially to each character of the message by the `join()` method. 
2. The resulting string is transformed to lower-case, unless the character is a vowel. In this case, the character is replaced by the character two places ahead of it in the English alphabet. The `ord()` method gives the numerical representation of a character, and adding 2 to this value returns the numerical representation of the desired character. The `chr()` method converts this numerical value back to a character.