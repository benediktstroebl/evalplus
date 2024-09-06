```python
def flip_case(string: str) -> str:
    return ''.join(char.swapcase() if char.islower() else char.swapcase() for char in string)
```

This script provides a function that takes a string as input and returns a new string with flipped cases, as per the problem statement.