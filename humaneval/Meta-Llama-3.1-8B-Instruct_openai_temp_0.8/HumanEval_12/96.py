```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    
    Args:
    strings (List[str]): A list of strings
    
    Returns:
    Optional[str]: The longest string in the list or None if the list is empty
    """
    if not strings:  # Check if the list is empty
        return None
    else:
        return max(strings, key=len)  # Return the longest string


# Test cases
if __name__ == "__main__":
    print(longest([]))  # Should print: None
    print(longest(['a', 'b', 'c']))  # Should print: 'a'
    print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script uses the built-in `max()` function in Python, which returns the largest item in an iterable or the largest of two or more arguments. The `key` argument is used to determine which part of the objects to compare. In this case, we're using `len()` to find the length of each string. This way, the `max()` function returns the longest string in the list. If the list is empty, it returns `None` as specified in the problem description.