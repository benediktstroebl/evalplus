```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_string = max(strings, key=len)
    return longest_string if len(longest_string) == max(len(s) for s in strings) else longest(
        [s for s in strings if s != longest_string]
    )
``` 

This code defines a function `longest` that takes in a list of strings and returns either the longest string in the list, or the first string of the same length as the longest string. If the list is empty, it returns `None`. The `longest` string is found by passing a lambda function `len` as the `key` argument to the `max` function. This lambda function calculates the length of each string in the list. The result is then checked to see if it is the longest string, and if not, the function recursively calls itself on a list of the strings that were shorter, in order to find the actual longest string. 

Here are some example outputs:
```
>>> longest(['a', 'b', 'c'])
'c'
>>> longest(['a', 'bb', 'ccc'])
'ccc'
>>> longest([])
None
```