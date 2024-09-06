```python
def count_consonants(word):
    return sum(1 for char in word if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

def select_words(s, n):
    words = s.split()
    result = [word for word in words if count_consonants(word) == n]
    return result
```
The `count_consonants` helper function calculates the number of consonants in a given word, providing a concise and efficient way to determine the count without relying on additional libraries. 

The `select_words` function splits the input string into a list of words, and then iterates through the words, checking their consonant counts with the `count_consonants` helper. This enables the selection of words that match the desired consonant criteria.