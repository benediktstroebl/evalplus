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
    """Returns list of words containing exactly n consonants"""
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```
The `count_consonants` identifies the number of consonants in a given word, while `select_words` function processes each word in the string `s` and tests whether the count of consonants in each word is equal to `n` and if so, adds it to the result list. 

Here is an example usage of the functions to evaluate the problem statement:
```python
>>> select_words("Mary had a little lamb", 3)
['Mary', 'lamb']
>>> select_words("simple white space", 2)
[]
>>> select_words("Hello world", 4)
['world']
>>> select_words("Uncle sam", 3)
['Uncle']
```

This script successfully addresses the problem statement and aligns with the provided test cases. It defines two functions, `count_consonants` and `select_words`, to first calculate the number of consonants in a word and then to filter and return words from a string that contain exactly n consonants.