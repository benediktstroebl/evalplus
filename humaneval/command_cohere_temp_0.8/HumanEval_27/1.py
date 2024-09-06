```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that takes a string as input and returns a string with flipped case, where all lowercase characters are flipped to uppercase and all uppercase characters are flipped to lowercase. This is achieved using a list comprehension and the `swapcase()` method for alphabetic characters, and leaving non-alphabetic characters unchanged. The expected behavior is for the output to be 'hELLO' for the input 'Hello'.