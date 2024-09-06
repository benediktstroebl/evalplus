```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This code uses a list comprehension with a conditional statement to determine whether each character of the input string should be flipped case-wise. The `isalpha()` method checks if each character is alphabetic, and the `swapcase()` method is used to flip the case. For characters that are not alphabetic, they are retained as is.