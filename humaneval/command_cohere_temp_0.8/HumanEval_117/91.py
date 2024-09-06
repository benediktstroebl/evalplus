```python
def count_consonants(word):
    """
    Helper function to count the number of consonants in a word.
    """
    total = 0
    for char in word:
        if char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            total += 1
    return total
    
def select_words(s, n):
    """
    Returns a list of all words from string s that contain exactly n consonants.
    """
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```
The main function selects words from `s` that have exactly `n` consonants, and finally returns the list of such words.

This script assumes that the input string contains only letters and spaces, which is mentioned in the provided problem statement.