```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that accepts a string as input and returns a string where the case of letters has been flipped, excluding non-alphabetic characters. To achieve this, it uses a list comprehension with a conditional check to determine if each character is alphanumeric, then either swaps its case or remains unchanged using the `swapcase()` method. This method preserves numbers and special characters without modification.