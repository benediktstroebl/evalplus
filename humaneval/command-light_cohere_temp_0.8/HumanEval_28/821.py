```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings (List[str]): List of strings to concatenate

    Returns:
    str: Concatenated string
    """
    return "".join(strings)

# Test case: Concatenate empty list
print(concatenate([]))  # Output: ''

# Test case: Concatenate list of strings
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```
This script defines a function **concatenate** that takes a list of strings as input and returns the concatenated string. 
It uses the list comprehension to convert the input into a single string, which is then returned.

The test cases at the bottom of the script verify that the function works as expected.