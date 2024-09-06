```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: list of strings
    Returns:
        string
    """
    return ''.join(strings)

# Test case 1
test_strings = ['a', 'b', 'c']
result = concatenate(test_strings)
assert result == 'abc'

# Test case 2
empty_list = []
result = concatenate(empty_list)
assert result == ''

# Test case 3
single_string = "Hello World"
result = concatenate([single_string])
assert result == "Hello World"
```
The code defines a function `concatenate` that takes a list of strings and concatenates them into a single string. The test cases cover different scenarios: empty list, list of strings, and a single string. The test cases pass, confirming that the function works as expected.