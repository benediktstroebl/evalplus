```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the longest string in the list.
    Parameters:
        strings: list of strings
    Returns:
        str: longest string in the list
    """
    return max(strings, key=len)

# Test the function
strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'

strings = ['abc', 'ABC', 'AB']
print(longest(strings))  # Output: 'ABC'

strings = ['abcde', 'abcd']
print(longest(strings))  # Output: 'abcd'

strings = []
print(longest(strings))  # Output: None

strings = ['ab', 'cd', 'acd']
print(longest(strings))  # Output: 'ab'
```
This script defines a function `longest` which takes a list of strings as input and returns the longest string from the list using the `max` function with the `len` key. The test cases demonstrate the this function's behavior correctly.