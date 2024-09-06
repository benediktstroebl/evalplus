```python
def flip_case(string: str) -> str:
    return ''.join(char.swapcase() if len(char) == 1 else char for char in string)
```

This script defines a function `flip_case` that accepts a string as an argument and returns a string that toggles the case of every character relative to its length, yielding the desired result. This algorithm achieves the functionality in a single pass without the need for duplicating the original string.