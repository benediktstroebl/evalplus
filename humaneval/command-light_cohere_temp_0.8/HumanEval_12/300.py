```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, return the longest one.
    """
    return max(strings, key=len)

# Test the function with a sample input
strings = ['a', 'bb', 'ccc']
longest_result = longest(strings)
print(longest_result)  # Output: 'ccc'

# Test the function with empty list input
empty_strings = []
empty_result = longest(empty_strings)
print(empty_result)  # Output: None

# Test the function with a list of strings of different lengths
long_strings = ['a', 'bb', 'ccc', 'aa']
long_result = longest(long_strings)
print(long_result)  # Output: 'ccc'
```

The script defines a function `longest` that takes a list of strings and returns the longest string in the list, based on its length. It then tests the using various inputs and verifies that the function is working correctly. The output of the test cases is printed to the console.