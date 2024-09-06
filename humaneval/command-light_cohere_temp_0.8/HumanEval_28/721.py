```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: List of strings to concatenate
    Returns:
    concatenated string
    """
    return "".join(strings)

# Example usage
strings = ["a", "b", "c"]
result = concatenate(strings)
print(result)  # Output: 'abc'
```
This script defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. It uses the `join string.join` to join all strings together into a single string, which is the return value. 

The example usage demonstrates how to call the `concatenate` function with a list of strings and print the result.