```python
def count_consonants(word):
    cc = 0
    for c in word:
        if c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            cc += 1
    return cc

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        cc = count_consonants(word)
        if cc == n:
            result.append(word)
    return result
```
The `count_consonants` helper function calculates the number of consonants in a given word, while the main `select_words` function splits the input string into a list of words, iterates through each word, and computes its total consonant count. If the count matches the specified requirement, the word is added to the result list, which is then returned. This solution adheres to the given constraints and successfully identifies words with exactly n consonants.