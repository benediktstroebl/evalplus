```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This code uses a list comprehension with a conditional statement to determine whether each character of the input string should be flipped case-wise. The `isalpha()` method checks if each character is alphanumeric, and the `swapcase()` method swaps the character's case if it is.