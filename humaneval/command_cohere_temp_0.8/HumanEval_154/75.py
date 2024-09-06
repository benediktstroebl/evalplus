```python
def cycpattern_check(first, second):
    return second in rotated_words(first)

def rotated_words(word):
    return ['', word[i:] + word[:i] for i in range(len(word))]
```