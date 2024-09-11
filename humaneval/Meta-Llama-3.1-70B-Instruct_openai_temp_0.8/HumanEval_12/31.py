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
        # If the list is empty, return None
        return None

    # Initialize the longest string with the first string in the list
    longest_str = strings[0]

    # Iterate over the list of strings
    for string in strings:
        # If the current string is longer than the longest string, update the longest string
        if len(string) > len(longest_str):
            longest_str = string

    # Return the longest string
    return longest_str


# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```