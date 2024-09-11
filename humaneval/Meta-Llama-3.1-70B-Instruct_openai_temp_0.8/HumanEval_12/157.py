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

    # If the list is empty, return None immediately
    if not strings:
        return None

    # Initialize the longest string to the first string in the list
    longest_str = strings[0]

    # Iterate over the rest of the strings in the list
    for string in strings[1:]:
        # If the current string is longer than the longest string found so far, update longest_str
        if len(string) > len(longest_str):
            longest_str = string

    # At this point, longest_str is the longest string in the list. Return it.
    return longest_str


# Example use cases:
print(longest([]))  # Should print None
print(longest(['a', 'b', 'c']))  # Should print 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print 'ccc'
```