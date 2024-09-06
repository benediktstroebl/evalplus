```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Returns the longest string from a list of strings."""
    if not strings:
        return None
    return max(strings, key=len)

# Test the function
print(longest(['a', 'b', 'c']))  # Output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
print(longest([]))  # Output: None
```
The function `longest` takes a list of strings as input and returns the longest string in the list. This is also returns `None` if the input list is empty. The function utilizes the max function with the `key=len` argument, which sets the maximum of the string to the length of the string. The test cases are then passing the test function.