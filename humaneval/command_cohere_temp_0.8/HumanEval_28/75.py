```python
# Importing the required module
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

# Test list with strings
test_cases.append((['a', 'b', 'c'], 'abc'))

# Checking the function against test cases
for strings, expected in test_cases:
    assert concatenate(strings) == expected
```

This script includes a function called `concatenate` that takes a list of strings as input and provides a single concatenated string as output. It addresses the scenario of an empty input list and successfully combines strings from a non-empty list. The function is then validated against sample tests, ensuring its effectiveness against both empty and non-empty lists.