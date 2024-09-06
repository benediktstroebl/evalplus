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

# Test the function with an empty list
test_concatenate([])
# Test the function with list of strings
test_concatenate(['a', 'b', 'c'])
# Test the function with list of strings with one element
test_concatenate(['c'])
```
This Python script defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. The function uses the same list comprehension to concatenate the strings and convert the result to a string. The function is then tested with three different cases: an empty list, a list with two strings, and a list with one string.