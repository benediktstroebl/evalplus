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
# Empty list
test_empty_list = []
result_empty_list = concatenate(test_empty_list)
assert result_empty_list == ''

# Non-empty list
test_non_empty_list = ['a', 'b', 'c']
result_non_empty_list = concatenate(test_non_empty_list)
assert result_non_empty_list == 'abc'
```

The `concatenate` function iterates through the list of strings and appends each string to the `result` variable. Finally, it returns the aggregated `result` string. The empty list test verifies that the function handles an empty list gracefully, resulting in an empty string. Meanwhile, the non-empty list test proves that the function correctly concatenates different strings in a list.