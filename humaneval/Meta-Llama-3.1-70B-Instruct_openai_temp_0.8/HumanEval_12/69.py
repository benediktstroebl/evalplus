```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    >>> longest([]) is None
    True
    >>> longest(['a', 'b', 'c']) == 'a'
    True
    >>> longest(['a', 'bb', 'ccc']) == 'ccc'
    True
    """

    # Check if the input list is empty
    if not strings:
        return None

    # Initialize the longest string with the first string in the list
    longest_str = strings[0]

    # Iterate over the rest of the strings in the list
    for string in strings[1:]:
        # If the current string is longer than the longest string, update the longest string
        if len(string) > len(longest_str):
            longest_str = string

    # Return the longest string
    return longest_str


# Test cases
if longest([]) is None:
    print("Test case 1 passed")
if longest(['a', 'b', 'c']) == 'a':
    print("Test case 2 passed")
if longest(['a', 'bb', 'ccc']) == 'ccc':
    print("Test case 3 passed")
```