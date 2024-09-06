```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.islower() else c for c in string)
```

This script provides a function that takes a string as an argument and flips the case of its characters. It checks if each character is lowercase using the `islower()` method and, if so, swaps its case using the `swapcase()` method. If the character is already uppercase, it remains as is. Ultimately, the function returns the string with the characters flipped as needed.