```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that accepts a string as an argument and returns a new string where the case of letters has been flipped. It employs a list comprehension that checks if each character is alphabetic using the `isalpha()` string method. When a character is alphabetic, it uses the `swapcase()` method to flip the case. For non-alphabetic characters like punctuation, the original character is retained in the output.