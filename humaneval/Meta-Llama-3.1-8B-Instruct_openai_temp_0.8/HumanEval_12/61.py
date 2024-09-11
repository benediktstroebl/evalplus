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
        return None  # Return None if the list is empty

    return max(strings, key=len)  # Return the longest string

# Test cases
if __name__ == "__main__":
    assert longest([]) is None
    assert longest(['a', 'b', 'c']) == 'a'
    assert longest(['a', 'bb', 'ccc']) == 'ccc'
```

In this script, we utilize the built-in `max` function in Python, which returns the largest item in an iterable or the largest of two or more arguments. We pass a `key` argument to `max` to specify that we want to find the longest string based on the `len` function, which returns the number of characters in a string. If the input list is empty, we return `None` as specified in the problem statement.