```python
def cycpattern_check(first, second):
    return second in rotated_words(first)

def rotated_words(word):
    return ['', word[i:]] + ([word[i:] + word[:i]] for i in range(1, len(word) + 1))
```

The `cycpattern_check` function uses the `rotated_words` function to generate all possible rotations of the second word and checks if any of these rotations are substring in the first word. 

The `rotated_words` function generates all possible rotations of a word.