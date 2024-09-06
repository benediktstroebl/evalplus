```python
def count_consonants(word):
    return sum(1 for char in word if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

def select_words(s, n):
    words = s.split()
    result = [word for word in words if count_consonants(word) == n]
    return result
```
The `count_consonants` helper function calculates the number of consonants in a given word, providing a clean and efficient way to determine the count without repeated iterators. The `select_words` function splits the input string into words and then filters the list using the helper function, effectively retrieving words with the desired consonant count. This approach ensures readability and optimizes the consonant-counting process.