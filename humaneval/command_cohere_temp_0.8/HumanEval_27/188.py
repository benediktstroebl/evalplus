```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.islower() else c for c in string)
```

This code uses a list comprehension with a conditional to determine whether each character of the string should be flipped to its swapped case or remained the same. The function ultimately returns the modified string.