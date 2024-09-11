```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    Args:
        strings (List[str]): The list of strings.

    Returns:
        Optional[str]: The longest string or None if the list is empty.
    """
    if not strings:
        return None
    
    return max(strings, key=len)

# Test cases
if __name__ == "__main__":
    assert longest([]) is None
    assert longest(['a', 'b', 'c']) == 'a'
    assert longest(['a', 'bb', 'ccc']) == 'ccc'
```

This script defines the `longest` function, which uses the built-in `max` function with the `key` argument set to `len` to find the longest string in the list. If the list is empty, it returns `None`. The test cases at the end verify that the function works correctly.