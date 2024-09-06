```python
from typing import List
def concatenate(strings: List[str]):
    """
    Concatenate list of strings into a single string and return the result.
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)

# Run unit tests
import pytest

# Test list of strings
test_strings = ['a', 'bb', 'ccc']

# Test empty list
assert concatenate([]), 'Should return empty string'

# Test single string
assert concatenate('test'), 'Should return single string'

# Test list of strings
assert concatenate(test_strings), 'Should concatenate correctly'
```
This Python script defines a function `concatenate` that takes a list of strings and returns their concatenation as a single string. It also includes unit tests using the test cases with various inputs to ensure the correctness of the function. You can expand this more test cases as needed to cover different scenarios.