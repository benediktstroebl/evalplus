```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatented string
    """
    return ''.join(strings)
# Example usage
strings = ['a', 'b', 'c']
result = concatenate(strings)
print(result) # Output: 'abc'
``` 
This code defines a function called `concatenate` that takes a list of strings as input and returns the concatenated string. The function uses the string concatenation with the help text, and the example usage demonstrates how to use the function to concatenate a list of strings into a single string.