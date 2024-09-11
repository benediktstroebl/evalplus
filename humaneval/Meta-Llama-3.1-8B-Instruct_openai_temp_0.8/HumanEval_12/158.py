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
    if not strings:
        return None
    else:
        return max(strings, key=len)


# Test cases
if __name__ == "__main__":
    print(longest([]))  # Should print: None

    print(longest(['a', 'b', 'c']))  # Should print: 'a'

    print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

In this script, the `longest` function uses the built-in `max` function with a `key` argument set to `len`. The `max` function returns the first string in the list with the maximum length in case of a tie, which meets the problem's requirements.