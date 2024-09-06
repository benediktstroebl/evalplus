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
# Test empty list
test_cases = [([], '')]

# Test single element
test_cases.append((['a'], 'a'))

# Test multiple elements
test_cases.append((['a', 'b', 'c'], 'abc'))

# Running the tests
for test_case in test_cases:
    assert concatenate(*test_case) == test_case[1]
```

The `concatenate` function iterates through each string in the input list and appends them to a result string, which is then returned. The test cases confirm that the function behaves as expected for empty, single-element, and multiple-element lists.