```python
def count_consonants(word):
    """
    This function counts the number of consonants in a given word.
    consonants are all letters except a, e, i, o, and u
    """
    count = 0
    for char in word:
        if char not in 'aeiou':
            count += 1
    return count

def select_words(s, n):
    """
    This function takes a string s and an integer n, returning a list of all words from s that contain exactly n consonants.
    If the string is empty or the number is invalid, an empty list is returned.
    """
    if not s:
        return []
    words = s.split(' ')
    result = []
    for word in words:
        if count_consonants(word) == n:
            result.append(word)
    return result
```
The `count_consonants` function is a utility function that calculates the number of consonants in a given word, which is used by the `select_words` function to filter and retrieve the words that contain exactly the specified number of consonants from the provided string `s`. 

Both functions are designed to efficiently solve the problem and provide accurate results.