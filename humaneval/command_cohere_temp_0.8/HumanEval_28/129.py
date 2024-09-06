```python
# Importing the required module
from typing import List


# Define the function
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    result = ""
    for string in strings:
        result += string
    return result


# Unit tests
def test_empty_list():
    # Empty list should return an empty string
    assert concatenate([]) == ""


def test_non_empty_list():
    # Non-empty list should return a concatenated string
    assert concatenate(["a", "b", "c"]) == "abc"


# Run the tests if the module is executed directly
if __name__ == "__main__":
    test_empty_list()
    test_non_empty_list()
```

This code includes the `concatenate` function and corresponding unit tests. The `test_empty_list` checks if an empty list is passed, then the function should return an empty string. The `test_non_empty_list` checks if a list of strings is passed, then the function should return a concatenated string. These tests ensure the function works correctly under different scenarios.