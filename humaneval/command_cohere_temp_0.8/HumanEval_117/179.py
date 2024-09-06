```python
def count_consonants(word):
    return sum(1 for char in word if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

def select_words(s, n):
    words = s.split()
    result = [word for word in words if count_consonants(word) == n]
    return result
```
The provided Python script solves the problem by first defining a function `count_consonants` that calculates the number of consonants in a given word, using a generator expression. 

Then, the main function `select_words` splits the input string into a list of words and filters it based on the consonant count, using the `count_consonants` function. The list of words containing exactly `n` consonants is returned as a result.

This solution is efficient and accurately determines the number of consonants in words consisting of only letters and spaces, ensuring the desired word count is achieved.