```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    :param strings: A list of strings
    :return: The longest string in the list, or None if the list is empty
    """

    # Check if the input list is empty
    if not strings:
        return None

    # Use the built-in max function with a key function that returns the length of each string
    # This will return the first string with the maximum length
    return max(strings, key=len)


# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```