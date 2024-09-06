```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This code uses the swapcase function to convert alphabetic characters to their flip case counterparts, while leaving non-alphabetic characters unchanged. It achieves the desired effect of flipping the case of characters while maintaining consistency with the original string's special characters and spaces.