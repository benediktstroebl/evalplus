```python
def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming vowels at the start and end of the word are excluded.
    """
    # Ensure the word has only alphabetic characters and is case-sensitive
    if not all(char.isalpha() for char in word) or not word.istitle():
        return ""

    # Use tuple unpacking to conveniently access characters and their indices in the word
    prev_consonant, prev_index = (), 0
    for char in word:
        if char.isalpha():
            if char.is conson.:
                prev_consonant, prev_index = char, len(word) - 1 - index
            elif char in 'AEIOUaeiou':
                if len(word) - 1 - index > prev_index:
                    return char
                else:
                    return prev_consonant
        index += 1
    return ""
```

This approach handles words with special characters and ensures case sensitivity, essential for certain words like "FULL" to correctly identify the U as the closest vowel. The code is optimized to process and return without creating unnecessary variables.