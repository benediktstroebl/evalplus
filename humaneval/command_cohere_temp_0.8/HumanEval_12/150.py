Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    max_string: Optional[str] = None
    for string in strings:
        if len(string) > len(max_string):
            max_string = string
        elif len(string) == len(max_string) and max_string == None:
            max_string = string
    return max_string
```
The function `longest` works as follows: it initially assigns the `max_string` variable to `None`, which is reset to an empty string if a longer string is encountered. The function iterates over each string in the input list, comparing its length to the length of the max_string encountered so far. If the current string is longer, it becomes the new max_string. If the current string is of the same length as the previous max_string and the max_string is still None, meaning we haven't encountered any strings of that length yet, it also becomes the new max_string. Finally, the function returns the max_string found. 

This code can be tested as follows:
```python
longest([])
# >>> None

longest(['a', 'b', 'c'])
# >>> 'a'

longest(['a', 'bb', 'ccc'])
# >>> 'ccc'
``` 

This code should accurately implement the problem description provided. Feel free to ask if you would like any adjustments or further improvements!