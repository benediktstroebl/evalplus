```python
def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming consonants sandwiching it.
    """
    vowels = "AEIOUaeiou"
    # Remove starting and ending vowels:
    word = word.strip(vowels)
    if not word:
        return ""
    # Filter out all inner vowels:
    word = [c for c in word if c not in vowels]
    # Ensure there's at least one consonant left:
    if not word:
        return ""
    return next((c for c in word if c in vowels), "")
```

The approach here is to:
1. Strip vowels from the beginning and end of the word.
2. Filter out all inner vowels.
3. If there are no consonants remaining, return an empty string.
4. Otherwise, find the first vowel that hasn't been filtered out, or an empty string. 

This will identify the vowel that consonants are 'protecting' in the word provided.