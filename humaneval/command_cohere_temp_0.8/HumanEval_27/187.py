```python
def flip_case(string: str) -> str:
    return ''.join(char.swapcase() for char in string)
```
This script provides a function that takes a string as an input and returns a string with flipped case letters. The function `flip_case()` uses a list comprehension with a `swapcase()` method to invert the case of each character in the string, achieving the desired effect of flipping the case.