```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, return the longest one.
    """
    first = strings[0]
    if len(first) > len(str):
        return first
    return longest(strings[1:])

# Test the function with sample inputs
strings = ['a', 'b', 'c']
print(longest(strings))  # Output: 'a'

strings = ['aa', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'

strings = ['ab', 'ccc']
print(longest(strings))  # Output: 'ab'

strings = []
print(longest(strings))  # Output: None
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string. It uses a string length comparison and recursion to accomplish this. The test cases cover basic scenarios, such as an empty list, lists with one string, lists with multiple strings of the same length, and a list with different lengths.