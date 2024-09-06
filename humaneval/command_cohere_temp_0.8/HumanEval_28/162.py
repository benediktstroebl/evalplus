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
test_cases = [([], '')]
# List of strings
test_cases.append((['a', 'b', 'c'], 'abc'))

for test_case in test_cases:
    with assertEqual(test_case[1], concatenate(test_case[0])):
        pass
```

This code defines a function called `concatenate` that takes a list of strings as input and returns a single string that concatenates all the elements in the list. The function is designed to handle an empty list and includes documentation and sample tests to verify its functionality against different input conditions.