```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one.
    >>> str longest(['a', 'b', 'c'])
    'c'
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test cases
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
print(longest(['a', 'bb', 'ccc', 'a']))  # Output: 'a'
print(longest(['a', 'bcda', 'ebfd']))  # Output: 'ebfd'
print(longest(['abcde', 'ab']))  # Output: 'abcde'
print(longest([]))  # Output: None
```
The above code defines a function `longest` that takes a list of strings as input and returns the length of the longest string. 

In the test cases section, the function is tested with various input strings. The output of the function is printed, which corresponds to the longest string from the input list.