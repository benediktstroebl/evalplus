```python
def count_consonants(word):
    return sum(1 for char in word if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

def select_words(s, n):
    words = [word for word in s.split() if word]
    return [word for word in words if count_consonants(word) == n]
```
The `count_consonants` helps to calculate the number of consonants for a given word which can be handy for several problems related to consonants and vowels. The `select_words` uses this helper function to filter words that contain exactly *n* consonants.