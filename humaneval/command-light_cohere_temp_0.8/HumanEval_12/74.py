```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one or None if empty. """
    list of strings: List[str]
    if not strings:
        return None
    return max(strings, key=len)
# Tests
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
print(longest([]))  # Output: None
print(longest(['aa']))  # Output: 'aa'
print(longest(['abcde', 'efg']))  # Output: 'efg'
print(longest(['a', 'b'], None))  # Output: 'a'
``` 
This function, `longest`, takes a list of strings and returns the longest string in the list. It returns `None` if the list is empty. The `max` function is used with a `key` argument set to the length of each string in the list, to find the maximum length.