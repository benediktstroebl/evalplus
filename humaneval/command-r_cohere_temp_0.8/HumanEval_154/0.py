```python
def cycpattern_check(word1: str, word2: str) -> bool:
"""Returns True if word2 or any of its rotations is a substring of word1"""
    if len(word2) > len(word1):
        return False

    word2 += word2
    word1_set = set(word1)

    for i in range(len(word2)):
        if word2[i] in word1_set:
            if word1_set.issubset(set(word2[i:])):
                return True
            if word1_set.issubset(set(word2[i::len(word2)]))):
                return True

    return False
```