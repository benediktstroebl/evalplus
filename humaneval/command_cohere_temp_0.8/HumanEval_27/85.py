```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that takes a string as input and returns a string with flipped cases for alphabetic characters. The 'swapcase()`' function is used to invert the case of alphabetic characters, while non-alphabetic characters like punctuation or spaces are left unchanged. This is a more efficient and concise solution that achieves the desired outcome.