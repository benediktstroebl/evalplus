```python
def count_consonants(word):
    counts = {char: 1 for char in word if char in 'bcdfghjklmnpqrstvwxyz'}
    return sum(counts.values())

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        if count_consonants(word) == n:
            result.append(word)
    return result
```

The `count_consonants` helper function calculates the number of consonants in a given word, ensuring compatibility with the given problem. The `select_words` function then iterates through each word in the string and checks if the count of consonants matches the desired count `n`. If so, it adds the word to the result list. This solution strategically utilizes Python's character-based dictionary comprehension and the `split` function to efficiently tackle the task.