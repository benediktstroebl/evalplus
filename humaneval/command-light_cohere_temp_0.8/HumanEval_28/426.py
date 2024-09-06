```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: list of strings to concatenate
    Returns:
    string
    """
    return ''.join(strings)

# Example usage
strings = ["a", "b", "c"]
result = concatenate(strings)
print(result)  # Output: 'abc'
``` 
This script defines a `concatenate` function that takes a list of strings as an argument and returns the concatenated string. It uses the general Python syntax and is a self-contained way to solve the problem. 

Note that it uses the `typing` module to add type annotations, which allows for better code readability and helps catch potential type-related errors or bugs.