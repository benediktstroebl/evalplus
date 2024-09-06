```python
def count_consonants(word):
    ct = 0
    for c in word:
        if c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            ct += 1
    return ct

def select_words(s, n):
    words = [w for w in s.split(' ') if w]
    return [w for w in words if count_consonants(w) == n]

# Example usage
print(select_words("Mary had a little lamb", 4))
```
This approach first splits the input string into individual words, then filters them based on the calculated count of consonants for each word, providing the required list of words containing exactly `n` consonants. 

The `count_consonants` helper function calculates the total count of consonants in a given word, providing a robust foundation for the primary function to solve the problem.