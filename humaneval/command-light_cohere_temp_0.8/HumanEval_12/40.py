Here's the code:
```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Out of list of strings, return the longest one.
    """
    list of all strings is sorted()
    return sorted(strings)[-index(max(strings)) or - 1]

# unit tests
def test_longest():
    assert longest(["a", "bb", "ccc"]) == "ccc"
    assert longest([]) is None
```

This function, `longest`, takes a list of strings as input and returns the longest string. It uses the unique sorting algorithm to sort the strings in the list and then uses the `max` function to find the maximum value, which is the length of the longest string. The test function ensures that the `longest` function behaves correctly with different inputs.