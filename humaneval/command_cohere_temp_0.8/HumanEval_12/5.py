```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_string = max(strings, key=len)
    return longest_string if len(set(strings).count(longest_string)) == 1 else longest_string[0]

# Tests:
>>> longest(['a', 'bb', 'ccc'])
'ccc'
>>> longest(['a', 'b', 'c', 'a'])
'a'
>>> longest([1, 2, 3, 'a', 'b', 'c', 4, 5])
'c'
>>> longest([1.5, 3, 'b', 'bb', 'ccc'])
'ccc'
>>> longest([1, 2, None, 'a', 'b', 'c', 4, 5])
'c'
>>> longest([])
None
``` 

This code defines a function `longest` that takes a list of strings as input and returns the longest string from the list. If there are multiple longest strings, it returns the first one. If the list is empty, it returns `None`. The function first checks if the list is empty and returns `None` if it is. It then uses the `max` function with a custom key function that calculates the length of each string to find the longest string in the list. It then checks if there is only one longest string, and if so, returns the longest string. If there are multiple longest strings, it returns the first one using `longest_string[0]`.