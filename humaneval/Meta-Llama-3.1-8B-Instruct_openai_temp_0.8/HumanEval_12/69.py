```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string in the list, or None if the list is empty.
    """
    if not strings:
        return None  # Return None for an empty list
    longest_str = max(strings, key=len)  # Find the longest string
    return longest_str  # Return the longest string


# Test cases
if __name__ == "__main__":
    # Test empty list
    assert longest([]) is None

    # Test single element list
    assert longest(['a']) == 'a'

    # Test multiple elements list
    assert longest(['a', 'b', 'c']) == 'a'
    assert longest(['a', 'bb', 'ccc']) == 'ccc'
```

In this script, the `longest` function iterates over the list of strings to find the longest one. It returns `None` if the input list is empty. If there are multiple strings of the same length, it returns the first one. The test cases at the end verify the correctness of the function.