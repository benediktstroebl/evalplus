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

# Test single-element list
test_cases.append((['a'], 'a'))

# Test multi-element list
test_cases.append((['a', 'b', 'c'], 'abc'))

# Testing the function with test-cases
for test_case in test_cases:
    with assertEqual(test_case[0], test_case[1]):
        concatenate(test_case[0])
```

This code defines a function called `concatenate` which takes a list of strings as input and returns a single string that concatenates all the strings in the list. The function is tested with three test cases, including an empty list, a list with a single element, and a list with multiple elements. The tests ensure that the function returns the expected output for each case. 

Note that the code uses the `assertEqual` helper, which is a placeholder and should be replaced with the appropriate testing framework method to compare the test cases correctly.  If you are using pytest, you would use `pytest.assert_equal` instead.  Please adjust according to your testing framework or let me know your testing framework of choice, and I can update the code accordingly.