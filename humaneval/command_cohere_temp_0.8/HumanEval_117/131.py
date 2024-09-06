```python
def count_consonants(word):
    return sum(1 for char in word if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

def select_words(s, n):
    words = [word for word in s.split()]
    words = [word for word in words if count_consonants(word) == n]
    return words
```
The provided Python script implements the `select_words` function as per the problem statement. It first counts the consonants in each word using the `count_consonants` helper function, then filters the words accordingly. The function works as intended and returns the list of words from the input string that contain exactly `n` consonants in order of appearance. It addresses the edge cases where the input string is empty or doesn't have enough consonants.