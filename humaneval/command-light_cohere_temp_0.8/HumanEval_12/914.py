```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one
    Returns the first one in case of multiple strings of the same length
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test cases
my_strings = ['a', 'bb', 'ccc', 'a']
longest(my_strings) # Output: 'ccc'

my_strings = ['a', 'bb', 'ccc', 'a']
longest(['a']) # Output: 'a'

my_strings = ['a'] * 10
longest(my_strings) # Output: 'a'
```

This function `longest` takes a list of strings as input and returns the length of the longest string in the list. It does this by using the `max()` function with the `key=len` argument to determine the length of the longest string, and returns it as the output. 

To test the function, you can pass different lists of strings and compare the output with the expected longest string.