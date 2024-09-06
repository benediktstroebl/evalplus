```python
# Importing the necessary module
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
# Empty list
test_list = []
result = concatenate(test_list)
assert result == ''

# Single string
test_list = ['abc']
result = concatenate(test_list)
assert result == 'abc'

# Multiple strings
test_list = ['ab', 'cd', 'efg']
result = concatenate(test_list)
assert result == 'abcdefg'
```

This script includes a function called `concatenate` that takes a list of strings as input and returns a single string as output, which is the concatenation of all the strings in the list. It also includes some tests to validate its behavior against different input cases.