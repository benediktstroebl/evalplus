```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings to concatenate
    Returns:
        concatenated string
    """
    return ''.join(''.join(strings))

# Example usage:
strings = ['a', 'b', 'c']
result = concatenate(strings)
print(result) # Output: 'abc'
```
This Python script defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. The function uses the static method `join` to join the strings into a single string. The function is self-contained and passes the corresponding tests.