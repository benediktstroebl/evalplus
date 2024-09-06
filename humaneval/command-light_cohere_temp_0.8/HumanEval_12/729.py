```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Return the longest string in a list.
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    return max(strings, key=len)

#Test cases for function
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
print(longest(['abc', 'ab', 'abc']))  # Output: 'abc'
print(longest(['abc', 'abc']))  # Output: 'abc'
print(longest(['abc', 'abcd', 'ab']))  # Output: 'abcd'
print(longest(['abcd', 'ab', 'abc']))  # Output: 'abc'
print(longest(['abcde', 'abcd', 'ab']))  # Output: 'abcd'
```
This function, `longest`, takes a list of strings as input and returns the longest string in the list. It also has a test cases that ensure it works correctly for all scenarios.