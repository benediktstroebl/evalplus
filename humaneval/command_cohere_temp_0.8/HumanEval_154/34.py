```python
def cycpattern_check(word1, word2):
    """
    Checks if the second word or any of its rotations is a substring in the first word.
    Args:
        word1 (str): The first word
        word2 (str): The second word

    Returns:
        bool: True if word2 or any of its rotations is a substring in word1, otherwise False
    """
    word2 = word2 + word2
    return any(word2.startswith(w) for w in (word2, word2[1:], word2[2:],) if w in word1)
```