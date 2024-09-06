```python
def count_consonants(word):
    """
    Helper function to count the number of consonants in a word.
    """
    word = word.lower()
    total = 0
    for c in word:
        if c in 'bcdfghjklmnpqrstvwxyz':
            total += 1
    return total
    
def select_words(s, n):
    """
    Reimplemented function to select words containing exactly n consonants.
    """
    if not s:
        return []
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```
The `select_words` function iterates through each word in the provided string `s`. For each word, it uses the `count_consonants` helper function to count the number of consonants in that word, accounting for lowercase letters only. If the count of consonants matches the target number `n`, the word is added to the result list. The function returns the list of selected words that meet the criteria.

This approach ensures that the selected words contain exactly `n` consonants, as explained in the problem statement. It also maintains the order of words from the input string `s`. 

The `count_consonants` helper function is utilized to determine the total number of consonants in a given word, regardless of whether the word is uppercase or lowercase. This function ensures the correctness of the consonant counting process.