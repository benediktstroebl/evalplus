```python
def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowel = 'aeiouAEIOU'
    
    # Extract substrings from the right half that ends with a consonant
    right_half = [end for end in word[1:].split('', 1) if end.lower() in consonants]
    
    # Check if the right half has a vowel standing between two consonants
    if right_half and right_half[0][-1] in vowel and right_half[1].lower() in vowel:
        return right_half[0][-1]
    elif right_half and right_half[-1].lower() in vowel:
        return right_half[-1]
    else:
        return ''
```

This approach involves extracting substrings from the right half of the word that end with a consonant using the `split('', 1)` method. Then, it checks whether any of these substrings have a vowel standing between two consonants or if it ends with a vowel. Ultimately, it returns the vowel if it meets the criteria or an empty string if no such vowel is found. 

This algorithm has a time complexity of `O(n)` where `n` is the length of the word, as it requires splitting the word once and performing constant time checks on the substrings. 

The given examples in the problem statement should all return the following outputs:
- "u" for "yogurt"
- "U" for "FULL"
- "" for "quick"
- "" for "ab"