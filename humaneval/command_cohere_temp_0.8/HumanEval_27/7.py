```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that accepts a string as an argument and returns a new string with flipped cases for alphabetical characters. The `swapcase` method is used to flip cases for alphabetic characters, while non-alphabetic characters like punctuation marks or spaces are left unchanged. This ensures the script's effectiveness and efficiency in solving the problem.