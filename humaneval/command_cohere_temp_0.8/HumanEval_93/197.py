```python
def encode(message):
    vowels = 'aeiouAEIOU'
    swapped = ''.join(c.swapcase() if c.isalpha() else c for c in message)
    return swapped.translate(str.maketrans(vowels, vowels[2:] + vowels[:2]))
```

This code uses the `translate` method to replace all vowels with the 2nd letter ahead of their position in the English alphabet, as per the problem statement. Test cases are not included but are necessary to validate the functionality of the code. Do you want me to write additional lines to test this function?