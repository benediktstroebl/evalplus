```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script defines a function that takes a string as an input and returns a string with flipped case, ensuring that non-alphabetic characters remain unchanged.