```python
def count_consonants(word):
    consonants = sum(1 for c in word if c in 'bcdfghjklmnpqrstvwxyz')
    return consonants

def select_words(s, n):
    words = s.split()
    result = [word for word in words if count_consonants(word) == n]
    return result
```
The `count_consonants` helper function calculates the total count of consonants in a given word, which helps the main `select_words` function filter words according to their consonant counts. This problem's solution leverages list comprehension to iterate through words, calculating their consonant counts with the helper function. The result list stores the selected words that contain the exact number of consonants specified by the input parameter `n`.