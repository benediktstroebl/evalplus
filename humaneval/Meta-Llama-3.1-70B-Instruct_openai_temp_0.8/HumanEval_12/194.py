```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings: A list of strings.

    Returns:
        The longest string in the list, or None if the list is empty.
    """
    if not strings:  # Check if the list is empty
        return None

    # Use the max function with a key argument to find the longest string
    # The key argument specifies that the max function should compare the lengths of the strings
    longest_string = max(strings, key=len)

    return longest_string


# Test cases
if __name__ == "__main__":
    assert longest([]) is None
    assert longest(['a', 'b', 'c']) == 'a'
    assert longest(['a', 'bb', 'ccc']) == 'ccc'
    assert longest(['a', 'bb', 'ccc', 'dddd']) == 'dddd'
    assert longest(['longest']) == 'longest'
```