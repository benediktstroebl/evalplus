```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings

    Returns:
        Optional[str]: The longest string in the list, or None if the list is empty
    """
    # Check if the list is empty
    if not strings:
        return None
    
    # Find the maximum length and return the corresponding string
    return max(strings, key=len)


# Test cases
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

This script defines the `longest` function as described in the problem. The function uses the built-in `max` function with `key=len` to find the longest string. The `doctest` module is used to run the test cases at the end of the script.