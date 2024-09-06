Here's a self-contained Python script that solves the problem of concatenating list of strings into a single string:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings
    Returns:
        string
    """
    return ''.join(strings)

# Unit tests
test_concat = [
    ''.join(List(['a', 'b', 'c']))     # Should return 'abc'
    ''.join(List()))                  # Should return ''
]

def test_concatenate():
    actual_result = concatenate(test_concat)
    assert actual_result == 'abc'

if __name__ == "__main__":
    test_concatenate()
```

This script provides a function `concatenate` that takes a list of strings as input and concatenates them into a single string. The `test_concatenate` function contains a test case that verifies the correctness of the `concatenate` function.