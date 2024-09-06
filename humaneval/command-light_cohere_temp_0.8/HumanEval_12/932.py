```python
from typing import List
def longest(strings: List[str]):
    """ Outlines the longest string in the list
    """
    return max(strings, key=len)
# Test case 1
strings = ['a', 'b', 'c']
assert longest(strings) == 'a'

# Test case 2
strings = ['a', 'bb', 'ccc']
assert longest(strings) == 'ccc'
```
This script defines a function called `longest` that takes a list of strings as an argument and returns the longest string in that list. It uses the `max` function along with the `key` argument set to the length of the string, ensuring that the function returns the string with the maximum length.