```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings to concatenate
    Returns:
        concatenated string
    """
    return ''.join(strings)

# Example usage
strings = ['a', 'b', 'c']
print(concatenate(strings))  # Output: 'abc'
strings = []
print(concatenate(strings))  # Output: ''
```

The code defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. The `type` is applied to the function signature to specify that the input argument must be a list of strings. The output of the function is the concatenated string.