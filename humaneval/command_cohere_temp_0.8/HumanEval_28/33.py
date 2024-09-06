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
for test_case in test_cases:
    input_values = test_case[0]
    expected_result = test_case[1]

    # Assuming the function is called concatenate() for simplicity
    result = concatenate(input_values)
    try:
        assert result == expected_result
        print("Test case \"{}\" passed".format(test_case))
    except AssertionError:
        print("Test case \"{}\" failed".format(test_case))
```

This script defines a function called `concatenate()` which takes a list of strings as input and returns a single string that concatenates all the inputs together. The script also includes sample tests, and for each test case, it checks if the result of the `concatenate()` function matches the expected result. If they match, it indicates a pass; otherwise, it indicates a failure. 
The `assert` statement is used to compare the actual and expected results of the concatenate function for each test case, and outputs whether the test case passes or fails based on this comparison.

Please note that this script assumes that the list of strings passed to the `concatenate()` function is already sorted alphabetically, as mentioned in the comments. If your list is not sorted, you may need to address that before concatenating the strings.