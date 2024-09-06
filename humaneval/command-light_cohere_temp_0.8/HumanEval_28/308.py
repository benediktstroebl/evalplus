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

# Test the function with an empty list
print(concatenate([]))  # Output: ''

# Test the function with a list of one string
print(concatenate(['a']))  # Output: 'a'

# Test the function with a list of three strings
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```
The function `concatenate` takes a list of strings as input and returns the concatenated string. The test cases ensure that the function works as expected. The output is the expected result.