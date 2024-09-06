```python
def encode(message):
    vowels = 'aeiouAEIOU'
    swapped = ''.join(letter.swapcase() for letter in message if letter.isalpha())
    encoded = ''.join(char if char not in vowels else vowels.find(char) + 2 for char in message)
    return swapped + encoded
```

This script defines a function `encode(message)`, which takes an input string message that is assumed to contain only letters.

The function first creates a string `vowels` that contains all the vowels (both lowercase and uppercase), and then uses a list comprehension to construct a new string `swapped` that contains each letter of the input message but with its case swapped if it is an alpha character (using the `swapcase()` method). Vowels are excluded from this process.

Next, another list comprehension is used to build the `encoded` string by walking through each character in the input message. If the character is not a vowel, it is left unchanged in the `encoded` string. Otherwise, it finds the index of the vowel character in the `vowels` string, adds 2 to this index (effectively skipping over the next two vowels in the alphabet), and uses this modified index to retrieve the corresponding character for inclusion in the `encoded` string.

Finally, the function returns the concatenation of `swapped` and `encoded` strings, effectively outputting the result of the desired encoding operation.