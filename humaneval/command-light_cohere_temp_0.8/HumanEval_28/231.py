```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate

    Returns:
        str: Concatenated string
    """
    return ''.join(strings)

# Test cases
strings = ['a', 'b', 'c']
result = concatenate(strings)
assert result == 'abc'
strings = []
result = concatenate(strings)
assert result == ''
```
This Python script defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. It uses the standard Python list concatenation `join` to combine the strings, and the test cases ensure that the function works as expected.