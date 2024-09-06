```python
def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming vowels at the start and end do not count.
    Empty string if no qualifying vowel is found.
    """
    # Ensure input is case-sensitive and lowercase
    word = word.lower()
    
    # Split the word into onsets and rimes (vowels are rimes)
    # e.g. "coat" becomes ["c", "oa", "t"]
    onsets = []
    rimes = []
    for char in word:
        if char in 'bcdfghjklmnpqrstvwxyz':
            onsets.append(char)
        elif char in 'aeiou':
            rimes.append(char)
    
    # Check each rime to see if it's surrounded by consonants
    # e.g. "cora" -> ["c", "o", "ra"]
    for i, rime in enumerate(rimes):
        if len(onsets) > i+1 and onsets[i+1] in 'bcdfghjklmnpqrstvwxyz' and onsets[i-1] in 'bcdfghjklmnpqrstvwxyz':
            return rime
    
    # No qualifying vowel was found
    return ""
```

This approach breaks the word into onsets (conservative consonants) and rimes (the vowels and the consonants after them), 
then it checks each rime to see if it's surrounded by consonants, returning the qualifying vowel if found. 

For the record, this problem can be solved in just a few lines thanks to Python's powerful string-handling capabilities. 

This solution assumes the input is valid; only English letters are present. To ensure this, the code could be wrapped in a try/except block and exceptions thrown for non-alphabetic characters.