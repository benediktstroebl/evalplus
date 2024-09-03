```python
def get_closest_vowel(word):
    """Returns the closest vowel between two consonants from the right side of the word.
    Vowels in the beginning or ending do not count. 
    Returns empty string if no such vowel is found. 
    """
    vowels = "AEIOUaeiou"
    last_consonant = None
    for c in word[::-1]:
        if c in vowels:
            return c
        else:
            last_consonant = c
            
    return ""
```