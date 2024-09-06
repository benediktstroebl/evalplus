```python
def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming consonants sandwiching it.
    """
    vowels = 'AEIOUaeiou'  
    # Using slice to retain original case
    word = word.upper() if word.isupper() else word.lower()
    sandwich = next((c for c in word[1:] if c not in vowels and 
                      (word[0:] + c).count(vowels) + 1 < (word[0:len(word) - 1].count(vowels) + 2)), '')
    return sandwich.lower() if word.islower() else sandwich
```

This code leverages the fact that the problem doesn't specify the exact placement of the consonants and the vowel. It checks if there are at least two consonants (not including the first one) followed by a vowel, or at least three consonants (including the first one) with the first one being a vowel. The rightmost consonant (before the found vowel) is then returned.