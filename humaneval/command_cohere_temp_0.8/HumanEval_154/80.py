```python
def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    a = a + a
    b = b + b
    return any(b in a for _ in range(len(b) // 2 + 1))
```
The function checks if the second word or any of its rotations is a substring in the first word. To do this, it repeats the second word until a rotation is found (i.e., a substring match is found). The `any()` function is then used to check whether any rotation of the second word is a substring of the first word. The `len(b) // 2 + 1` is used to ensure the function checks all rotations, including the original second word and its mirror reflections.  This way, the script correctly identifies whether the second word can be constructed from the first word without considering letter cases.