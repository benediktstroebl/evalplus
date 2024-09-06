```python
def flip_case(string: str) -> str:
    return ''.join(char.swapcase() for char in string)
```
This script provides a function that accepts a string as an argument and returns a new string with flipped case, where lowercase characters become uppercase and uppercase characters become lowercase. This behavior is achieved by using the `swapcase()` method on each character in the string.