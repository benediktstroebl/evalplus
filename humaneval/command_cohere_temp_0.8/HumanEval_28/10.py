```python
# Problem: Concatenate list of strings into a single string

from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    Empty list returns empty string.
    """
    result = ''.join(strings)
    return result
```

This script defines a function `concatenate` that takes in a list of strings and returns a single string that concatenates the inputs. The function is designed to handle an empty list as input, in which case it returns an empty string. Two test cases are provided to demonstrate the function's behavior.

The implementation utilizes the `join` method to concatenate the strings in the list. For an empty list, join returns an empty string. This is in line with the function's behavior, as outlined in the problem description.

To verify the correctness of the `concatenate` function, the following tests can be executed:
```python
# Test Case: Empty list
assert concatenate([]) == ''

# Test Case: Non-empty list
assert concatenate(['a', 'b', 'c']) == 'abc'
```

These tests check for the function's behavior with both an empty list and a non-empty list of strings. The output of each test case is echoed to the console to confirm the function's correctness.