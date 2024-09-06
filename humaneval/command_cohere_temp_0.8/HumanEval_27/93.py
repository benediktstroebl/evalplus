```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This code uses the swapcase function to convert all characters to their flip case counterpart, but for non-alphabetic characters, it remains unchanged. The join function is then used to combine the modified characters into a single string.