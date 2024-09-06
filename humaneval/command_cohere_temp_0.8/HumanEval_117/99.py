```python
def count_consonants(word):
    """Count consonants in a word"""
    word = word.lower()
    total = 0
    for char in word:
        if char in "bcdfghjklmnpqrstvwxyz":
            total += 1
    return total

def select_words(s, n):
    """Return list of words with exactly n consonants"""
    words = s.split()
    result = []
    for word in words:
        count = count_consonants(word)
        if count == n:
            result.append(word)
    return result
```
The approach uses the `count_consonants` helper function to determine the total consonants in each word as the first step. This is followed by a loop that iterates through all words in the string and adds them to the result list if they contain exactly n consonants. Ultimately, this gives us the list of words with the specified quantity of consonants from the original string.