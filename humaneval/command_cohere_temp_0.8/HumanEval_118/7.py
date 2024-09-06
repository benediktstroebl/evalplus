```python
def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowel = 'aeiouAEIOU'
    
    # Extract substrings after the last consonant and before the first vowel from the end
    for last_consonant_idx in range(len(word) - 2, -1, -1):
        if word[last_consonant_idx] not in consonants:
            continue
        substring = word[last_consonant_idx + 1:]
        if any(char in vowel for char in substring):
            return substring[::-1][0] if substring else ''

    # If no matching vowel found from the previous logic, try the whole word
    if any(char in vowel for char in word):
        return word
    
    return ''
```

This script employs two arrays for consonant and vowel characters to iterate over a given `word`. It identifies substrings after the last consonant and before the first vowel from the right side of the word using a loop. The reverse of this substring is taken to check if it starts with a vowel, addressing cases like 'FULL' where the first vowel is capitalized. If no such vowel is found, it checks if the whole word has any vowels.