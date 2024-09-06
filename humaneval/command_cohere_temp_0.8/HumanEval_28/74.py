```python
# Import the necessary module
from typing import List


# Define the function
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    result = ''
    for string in strings:
        result += string
    return result


# Intrinsic Docstring and Example Tests
# -------------------------------------
def test_concatenate_empty_list():
    """
    Test the handling of an empty list.
    """
    assert concatenate([]) == ''


def test_concatenate_non_empty_list():
    """
    Test the concatenation of a list with elements.
    """
    assert concatenate(['a', 'b', 'c']) == 'abc'


# Run the tests
test_concatenate_empty_list()
test_concatenate_non_empty_list()
```

The above Python code provides a self-contained function `concatenate` that concatenates a list of strings into a single string and includes self-contained tests in the docstrings of the provided test functions that validate the behavior of the `concatenate` function.

The `concatenate` function iterates through each string in the input list and appends them to a result string, which then returns the combined result. The test cases included validate both an empty list input and a non-empty list input to cover the basic functionality of the `concatenate` function.