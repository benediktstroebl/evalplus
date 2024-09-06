```python
# Importing required module
from typing import List


# Defining the function
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    result = ''
    for string in strings:
        result += string
    return result


# Sample tests
# Test empty list
test_cases = [([], '')]
# Test single element list
test_cases.append((['a'], 'a'))
# Test multiple elements list
test_cases.append((['a', 'b', 'c'], 'abc'))

# Checking the function against test cases
for strings, expected in test_cases:
    assert concatenate(strings) == expected
```

This script includes a function called `concatenate` that takes a list of strings as input and provides a single concatenated string as output. It is tested against different scenarios, namely an empty list, a list with a single element, and a list with multiple elements, all of which return expected outputs.