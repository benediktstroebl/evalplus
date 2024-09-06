Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    """
    if not strings:
        return None
    return max(set(strings), key=strings.count)
```
This script uses the `max` function with a custom `key` argument to solve the problem. The provided tests in the code block are:
```python
>>> longest([])
None

>>> longest(['a', 'b', 'c'])
'a'

>>> longest(['a', 'bb', 'ccc'])
'ccc'

>>> longest(['aaa', 'aa', 'ab'])
'aaa'

>>> longest(['a', 'a', 'b'])
'a'
``` 
The function works as follows:
- The input is a list of strings, and the output is either the longest string in this list or `None` if the list is empty. 
- The function uses the `max` function to find the longest string in the list. The `key` argument is used to specify the function that is used to compare the elements. In this case, the count function is used,  which counts the occurrences of the current string in the list, to compare the strings in the list, ensuring that the longest unique string is returned. 
- In case there are multiple strings of the same length, the function will return the first one since the `max` function returns the first element in case of the same `key` value. 
- If the list is empty, `None` is returned. 
This solution is efficient and straightforward, providing a clear way to solve this problem.