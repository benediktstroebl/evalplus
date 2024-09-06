```python
def count_consonants(word):
    consonants = 0
    for char in word:
        if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            consonants += 1
    return consonants

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        if count_consonants(word) == n:
            result.append(word)
    return result
```
The `count_consonants` helper function calculates the number of consonants in a given word, while the main `select_words` function splits the input string into words, iterates through them, and retains those with the desired consonant count. This solution adheres to the problem statement's guidelines, including the input string's letter-only and whitespace assumptions.