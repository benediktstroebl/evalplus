```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This code uses the swapcase function to convert all characters to their flipped case except for non-alphabetic characters, which are retained as-is. This approach avoids the complexity of having to check whether characters are already in the correct case, making the code more efficient and easier to understand.