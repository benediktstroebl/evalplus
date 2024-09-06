```python
from typing import List
def longest(strings: List[str]): 
    """
    Returns the longest string in the list.
    >>> longest(['a', 'bc'])
    'a'
    """
    if not strings: 
        return None
    return max(strings, key=len)

# Test cases
strings = ['a', 'bc', 'abc']
print(longest(strings)) 
# Output:  'abc'
strings = ['', 'a', 'bb', 'ccc']
print(longest(strings)) 
# Output:  'ccc'
strings = ['a', 'bb']
print(longest(strings)) 
# Output:  'bb'
```
This script defines a function `longest` that takes a list of strings as an argument and returns the longest string in the list. It also includes a test cases to verify the function.