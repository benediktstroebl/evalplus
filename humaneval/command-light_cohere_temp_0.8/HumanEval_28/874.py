```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    :type strings: List[str]
    :rtype: str
    """
    return ''.join(strings)

# Test case 1
strings = ["a", "b", "c"]
result = concatenate(strings)
print(result)  # Output: 'abc'

# Test case 2
empty_strings = []
result = concatenate(empty_strings)
print(result)  # Output: ''

# Test case 3
strings = ["a", "bc", "d"]
result = concatenate(strings)
print(result)  # Output: 'abcd'
```
This script provides a function `concatenate` that takes a list of strings as input and concatenates them into a single string, passing corresponding tests to ensure the correctness of the function.