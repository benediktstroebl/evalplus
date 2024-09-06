```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings
    Returns:
        str: concatenated string
    """
    return ''.join(strings)

# Test the function with valid inputs and validate the output
strings = ['a', 'bc', '']
result = concatenate(strings)
assert result == 'abc'

# Test the function with empty input and validate the output
empty_strings = []
result = concatenate(empty_strings)
assert result == ''
```
The code defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. The function is then passed to the test cases with both valid and empty strings, and the output is validated using assertion.