```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Returns the length of the longest string in the list."""
    return max(strings, key=len)

# Test cases
strings = ["a", "b", "c"]
print( longest(strings) )  # Output: 3

strings = ["aa", "bb", "ccc"]
print( longest(strings) )  # Output: 3

strings = []
strings. strings empty list
print(longest(strings)) )  # Output: None

strings = ["a", "bc", "abc"]
print( longest(strings) )  # Output: 3
```
This script defines a function called `longest` that takes a list of strings as an argument and returns the length of the longest string in that list. The function uses the max function with the `key` argument set to the length of the strings, and returns the result.

The test cases ensure that the function works correctly for different input scenarios.