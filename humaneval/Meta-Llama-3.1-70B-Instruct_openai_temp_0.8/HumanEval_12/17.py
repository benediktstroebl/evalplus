```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.
    """
    if not strings:  # check if the list is empty
        return None
    
    # use the max function with the key argument set to len 
    # to find the longest string in the list
    # in case of multiple strings of the same length, max returns the first one
    return max(strings, key=len)

# test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```