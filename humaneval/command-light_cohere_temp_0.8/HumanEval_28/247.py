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

# Test the function with empty list
test_str = concatenate([])
assert test_str == ''

# Test the function with strings in the list
test_str = concatenate(['a', 'b', 'c'])
assert test_str == 'abc'
```
This Python code defines a function called `concatenate` that takes a list of strings as input and concatenates them into a single string. The function uses the example of using an empty list and a list with three strings to test the correctness of the `concatenate` function.