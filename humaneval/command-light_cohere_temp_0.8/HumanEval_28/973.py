```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concaten of strings in a single string
    """
    return ''.join(strings)

# Test case 1
test_strings = ['']
result = concatenate(test_strings)
assert result == ''

# Test case 2
test_strings = ['a', 'b', 'c']
result = concatenate(test_strings)
assert result == 'abc'

# Test case 3
test_strings = ['a', 'd']
result = concatenate(test_strings)
assert result == 'ad'
```

This Python code defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. The code also provides three test cases to verify the correctness of the `concatenate` function: it ensures that the empty string is returned for an empty list, that the concatenation works as expected for the list of uppercase letters, and that it concatenates the list of lowercase letters correctly.