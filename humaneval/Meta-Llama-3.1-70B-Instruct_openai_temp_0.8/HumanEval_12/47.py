```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
    strings (List[str]): A list of strings.

    Returns:
    Optional[str]: The longest string in the list, or None if the list is empty.
    """
    if not strings:
        # Return None if the input list is empty.
        return None

    # Use the max function with a key argument to find the longest string.
    # The key argument is a function that takes a string and returns its length.
    # In case of multiple strings of the same length, max will return the first one.
    return max(strings, key=len)


# Test cases
if __name__ == "__main__":
    assert longest([]) is None
    assert longest(['a', 'b', 'c']) == 'a'
    assert longest(['a', 'bb', 'ccc']) == 'ccc'
```