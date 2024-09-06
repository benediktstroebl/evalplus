```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.

    if not strings:
        return None

    longest_len = 0
    longest_str = ''

    for string in strings:
        if len(string) > longest_len:
            longest_len = len(string)
            longest_str = string

    return longest_str

#Test the function
>>> longest(['a', 'bb', 'ccc'])
'ccc'

>>> longest([])
None

>>> longest(['aa', 'aa', 'aa'])
'aa'

```
This Python code defines a function named `longest` that takes a list of strings as input and returns the longest string from the list. The function uses a `type hint` and `named parameters` to make the code more readable and clear. The function first checks if the list is empty, and returns `None` in that case. It then iterates over each string in the list and keeps track of the length of the longest string found so far. The function returns the longest string found in the list.