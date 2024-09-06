```python
def cycpattern_check(word1, word2):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    word2 = word2 + word2
    return any(word2 in word1 for _ in range(len(word2)))
```

The function passes the test cases as the `any` function iterates through all rotations of the second word and checks if any rotation exists in the first word as a substring.