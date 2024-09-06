```python
def flip_case(string: str) -> str:
    return ''.join(char.swapcase() if len(char) == 1 else char for char in string)
```

This script provides a function that takes a string as input and returns a new string where each lowercase character is flipped to uppercase and each uppercase character is flipped to lowercase. This function achieves this by using a list comprehension and the `swapcase()` method for individual characters, while ignoring characters with multiple letters.