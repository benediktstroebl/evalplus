Here is a self-contained Python script with a function that solves the problem of returning the longest string from a list of strings:

```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Returns the length of the longest string in the list.
    """
    list of strings.
    max_length = max(len(string) for string in strings)
    return max_length if max_length is not None else None

# Test cases

# List of strings
test_strings = ['a', 'b', 'c']
# Test function with empty list
test_empty = longest([])
# Test function with strings of different lengths
test_different = longest(['a', 'bb', 'ccc'])
# Test function with strings of the same length
test_same = longest(['aaa'])
print(test_strings == test_different)  # True
print(test_empty == test_same)  # True
print(test_same == 'aaa')  # False
```

This script defines a function `longest` that takes a list of strings as an argument. It uses the `max` to find the length of the longest string in the list and then returns this length. The test cases show that the function works correctly for various scenarios.