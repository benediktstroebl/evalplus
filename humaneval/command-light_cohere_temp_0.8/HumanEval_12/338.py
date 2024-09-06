Here's a self-contained Python function that solves the problem you provided:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Find the longest string from the list.
    """
    The expected input to be a list of strings.
    """
    return max(strings, key=len)
    """

# Unit tests
def test_longest():
    assert longest(["a", "bb", "ccc"]) == "ccc"

def test_empty_list():
    assert not(longest([]))

# Example usage
strings = ["a", "bb", "ccc"]
print(longest(strings))
```
This script defines a function `longest` that takes a list of strings and returns the longest string. It is then a test functions to verify the function's correctness, and provide examples of usage.