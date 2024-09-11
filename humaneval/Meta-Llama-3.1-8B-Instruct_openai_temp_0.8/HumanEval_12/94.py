```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings

    Returns:
        Optional[str]: The longest string in the list, or None if the list is empty
    """
    if not strings:
        return None
    return max(strings, key=len)


# Example usage:
if __name__ == "__main__":
    print(longest([]))  # Output: None

    print(longest(['a', 'b', 'c']))  # Output: 'a'
    print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
```

This script defines the `longest` function which takes a list of strings and returns the longest one. It uses the built-in `max` function with the `key=len` argument to find the longest string, returning the first one in case of a tie. The example usage at the end demonstrates the function's behavior.