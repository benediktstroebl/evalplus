```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    :param strings: List of strings to concatenate
    :return: Concatenated string
    """
    return ''.join(strings)

# Test the function
strings = ['a', 'b', 'c']
result = concatenate(strings)
assert result == 'abc'

# Test the function with empty list
strings = []
result = concatenate(strings)
assert result == ''
```
This code defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. The test cases at the time verify that the function works correctly for both empty and non-empty strings. The function is tested with an actual string and an empty list, and the test assertions verify the expected outputs.