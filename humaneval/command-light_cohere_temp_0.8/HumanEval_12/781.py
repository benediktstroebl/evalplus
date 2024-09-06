```python
from typing import List
def longest(strings: List[str]):
    """ Outlines a list of strings, returns the longest one.

    # create a string to be compared to all strings
    combined = ''.join(''.join(strings)
    # compare the length of combined to all input strings
    if combined.isep(len(strings)):
        return None
    else:
        # return the length of the longest string
        return max(map(len,strings))

# test the function
>>> longest(['a', 'bb', 'ccc'])
'ccc'
>>> longest(['a'])
None
>>> longest(['aa'])
'a')
>>> longest([])
None
```