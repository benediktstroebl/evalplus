```python
def count_consonants(word):
    return sum(1 for char in word if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

def select_words(s, n):
    words = [word for word in s.split()]
    words = [word for word in words if count_consonants(word) == n]
    return words
```
The `count_consonants` helps determine the number of consonants for a given word which is later used with the main function `select_words` to filter words based on the number of consonants. This solution passes all the test cases mentioned in the problem.