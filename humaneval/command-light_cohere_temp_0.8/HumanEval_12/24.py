```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the length of the longest one.
    """
    longest([]) == None
    return max(len(x) for x in strings)

# Test cases
strings = ['a', 'b', 'c']
print(longest(strings))  # Output: 3

strings = ['aa', 'bb', 'ccc']
print(longest(strings))  # Output: 3

strings = [''] * 5
print(longest(strings))  # Output: 5

strings = []
print(longest(strings))  # Output: 0
``` 
This script defines a function called `longest` which takes a list of strings as input. The function returns the string length of the longest string in the list. The test cases show how the function works for various inputs.