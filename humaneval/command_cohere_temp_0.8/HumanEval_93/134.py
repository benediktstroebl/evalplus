```python
def encode(message):
    vowels = 'aeiouAEIOU'
    swapped = ''.join(letter.swapcase() if letter.isalpha() else letter for letter in message)
    return swapped.translate(str.maketrans(vowels, vowels[2:] + vowels[:2]))
```

This code uses the `str.translate()` method to replace vowels with the 2nd letter ahead in the English alphabet, and swaps the case of other letters. The maketrans function is used to create a translation table that performs the 2nd letter transformation on the vowels. This approach is both concise and efficient, achieving the desired output in a single line of code.