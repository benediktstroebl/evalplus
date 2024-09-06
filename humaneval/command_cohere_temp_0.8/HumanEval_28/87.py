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

# Test list with strings
test_cases.append((['a', 'b', 'c'], 'abc'))

# Checking the function against test cases
for inputs, expected in test_cases:
    output = concatenate(inputs)
    if output == expected:
        print('Test passed!')
    else:
        print('Test failed!')
```

The tests check if the output of the `concatenate()` function matches the expected result for different input scenarios. 

You can add more test cases to ensure the function behaves as expected for different inputs. Let me know if you want to test for specific scenarios!