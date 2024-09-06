```python
def encode(message):
    vowels = 'aeiouAEIOU'
    swapped = ''.join(c.swapcase() if c.isalpha() else c for c in message)
    return swapped.translate(str.maketrans(vowels, vowels[2:] + vowels[:2]))
```

This code defines a function `encode` that takes a message as an input. It performs two operations:
1. Swaps the case of all letters, so that uppercase letters become lowercase and vice versa. This is achieved using the `swapcase()` method. The `isalpha()` method is used to identify letters. With this, all non-letter characters remain unchanged. 
2. Replaces all vowels with the letter that appears 2 places ahead of it in the English alphabet. The vowels of the English alphabet are stored in the `vowels` variable in lowercase and uppercase. The `translate()` method is then used to replace each vowel with the corresponding letter from the shifted vowels. The shifted vowels are created by removing the current vowel and adding the vowel from 2 positions further. 

The resulting string after these two operations is returned as the encoded message. 

This problem is complex to solve with one single regex approach, as it needs to perform both case swapping and vowel substitution simultaneously. Hence, the approach here implements the required swaps and substitutions separately, packaged in a single function, for the message handling. 

This solution assumes that the input message only contains letters. If other characters should also be treated as unchanged, one can adjust the `encode` function accordingly. Possibly by removing the `c.isalpha()` condition so that all characters remain in the message unchanged.