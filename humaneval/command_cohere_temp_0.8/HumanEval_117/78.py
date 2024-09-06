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
        cnt = count_consonants(word)
        if cnt == n:
            result.append(word)
    return result
```
The `count_consonants` counts the number of consonants in a word, while `select_words` splits the input string into words, counts the consonants in each word, and selects the words with exactly `n` consonants as requested. 

Here is an example usage of the code:
```python
select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
```

This will return the result ['Mary', 'lamb'], as they are the words in the sentence that contain exactly 3 consonants.