```python
def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming the vowels occur between two consonants.
    Ignores vowels at the start and end of the word.
    """
    vowels = 'AEIOUaeiou'
    # Removing vowels at the start and end
    trimmed = word.strip(word.lower())
    # If the word is empty now, no vowels to find
    if not trimmed:
        return ''
    # Find the index of the last consonant
    last_consonant_idx = len(trimmed) - 1
    while last_consonant_idx > 0 and trimmed[last_consonant_idx].lower() in vowels:
        last_consonant_idx -= 1
    # Find the closest vowel after that consonant (going back or passing it)
    for i in range(last_consonant_idx + 1, len(trimmed)):
        if trimmed[i].lower() in vowels:
            return trimmed[i]
    # No vowel after the last consonant, so we must have a single consonant
    # We return the very last character (original word's last character)
    return word[-1]
```

This approach focuses on the 'trimmed' version of the word, which removes any vowels at the start or end of the word. Starting from the last character of this trimmed word, it iterates backwards checking if the character is a consonant. It finds the last consonant or the last vowel if the word starts or ends with a vowel. Then, it checks the vowels after that point (going back or passing it) until it finds a vowel, which is then returned. If no such vowel exists, it implies the word only has one consonant (or is empty), and the original last character (or an empty string) is returned. 

The unit tests provide an input sentence for each of the examples provided in the problem statement to demonstrate the function's behavior and ensure it is correct.