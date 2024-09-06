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
    """Return list of words containing exactly n consonants"""
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```
The `count_consonants` identifies the number of consonants in a given word, while `select_words` function processes each word in the string `s` and tests whether the count of consonants in each word matches the target `n`, if so, the word is added to the result list. 

Both functions are designed to handle the input string containing only letters and spaces, as stated in the problem. 
This approach provides a concise solution to the specified problem and efficiently passes the described tests.