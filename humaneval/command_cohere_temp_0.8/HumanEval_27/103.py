```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.islower() else c.upper() for c in string)
```

This script defines a function `flip_case` that takes a string as an input and returns the same string with its characters flipped between uppercase and lowercase. It utilizes the `swapcase()` method to flip the case of lowercase characters and leaves uppercase characters unchanged, while uppercasing the remaining lowercase characters.