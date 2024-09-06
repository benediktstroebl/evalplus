```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script defines a function `flip_case` that takes a string as an input and flips the case of alphabetical characters, leaving non-alphabetical characters unchanged. It achieves this using a list comprehension with conditions based on the `isalpha()` and `swapcase()` string methods to flip the case of characters.

This solution is efficient and well-structured to handle various input scenarios, providing a clear and concise implementation of the problem's requirement.