```python
def encode(message):
    vowels = 'aeiouAEIOU'
    new_message = ''.join(
        c.swapcase() if c.isalpha() and c not in vowels else
        vowels.index(c) + 2 + vowels[vowels.index(c) + 1]
        for c in message
    )
    return new_message
```

This script defines a function `encode` that takes a message as an input. The function loops through each character in the input message. If the character is a letter and not a vowel, it is swapped case. If the character is a vowel, it is replaced by the character that is two places ahead of it in the English alphabet. The function then joins the modified characters into a new string and returns this new string.

This solution assumes only letters, reverting any other character or non-English letters unchanged. Also, there is no accounting for lowercase vowels in uppercase messages and vice-versa.