```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string """
    return ''.join() + ''.join(strings)

# Test case 1
test_strings = ['a', 'bc']
result = concatenate(test_strings)
assert result == 'abc'

# Test case 2
strings = []
result = concatenate(strings)
assert result == ''

# Test case 3
strings = ['a', 'bc', 'c']
result = concatenate(strings)
assert result == 'abc'
```
This code defines a function `concatenate` that takes a list of strings as an argument and concatenates them into a single string. It uses the specific type hints for better code readability and maintainability.