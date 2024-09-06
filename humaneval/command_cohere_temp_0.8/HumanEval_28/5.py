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
# Empty list
test_empty_list = ['']
assert concatenate(test_empty_list) == ''

# Single string
test_single_string = ['abc']
assert concatenate(test_single_string) == 'abc'

# Multiple strings
test_multiple_strings = ['a', 'b', 'c']
assert concatenate(test_multiple_strings) == 'abc'
```

The `concatenate` function iterates through the list of strings and appends each string to the `result` variable. Finally, it returns the `result` string.

The sample tests demonstrate its behaviour with an empty list, a list with a single string, and a list with multiple strings.  The output is an empty string for an empty list, and the concatenation of the strings in the list for lists with at least one element.  It's advisable to add more comprehensive tests to cover edge cases and validate the function's behavior against expectations.  This ensures the robustness of the solution.