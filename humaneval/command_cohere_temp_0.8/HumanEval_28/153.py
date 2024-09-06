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
test_empty = []
result_empty = concatenate(test_empty)
assert result_empty == ''

# Non-empty list
test_non_empty = ['a', 'b', 'c']
result_non_empty = concatenate(test_non_empty)
assert result_non_empty == 'abc'
```

The `concatenate` function iterates through the list of strings and appends each string to the `result` variable. The final value of `result` is then returned.

The test cases confirm that the function works as expected, handling both empty and non-empty lists of strings.