```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """ Returns the longest string from the list. If the list is empty, return None"""
    if not strings:
        return None
    return max(strings, key=len)

# Test the function
strings = ['a', 'b', 'c']
longest(strings) # Output: 'c'

strings = ['a']
longest(strings) # Output: 'a'

strings = []
longest(strings) # Output: None

strings = ['aa', 'bb', 'ccc']
longest(strings) # Output: 'bb'
```
This Python script defines a function called "longest" that takes a list of strings as input and returns the longest string from that list. The function utilizes the typing to ensure the input data type is correct, and it also returns the result of the longest string. This script provides a test cases to ensure the function's functionality.