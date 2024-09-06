```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings (List[str]): List of strings to concatenate

    Returns:
    str: Concatenated string
    """
    return ''.join(strings)
#Example usage
strings = ["a", "b", "c"]
print(concatenate(strings))  # Output: "abc"
``` 
This code defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. It uses the other `join` function to concatenate the strings into a single string and returns the result.