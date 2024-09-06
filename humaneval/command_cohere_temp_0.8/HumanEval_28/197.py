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

# Unit tests
def test_concatenate_empty_list():
    """
    Test case for an empty list.
    """
    assert concatenate([]) == ''

def test_concatenate_non_empty_list():
    """
    Test case for a non-empty list.
    """
    assert concatenate(['a', 'b', 'c']) == 'abc'

# Run the tests if the script is executed directly
if __name__ == "__main__":
    test_concatenate_empty_list()
    test_concatenate_non_empty_list()
```

This script includes the `concatenate` function and corresponding unit tests. The function iterates through the list of strings and concatenates them without the need for a separator. The tests verify the function's behavior for both an empty list and a non-empty list. When executed directly, the script runs the tests and displays the test results, which should show that both tests pass.