```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
    strings (List[str]): A list of strings.

    Returns:
    Optional[str]: The longest string in the list or None if the list is empty.
    """
    # Check if the input list is empty
    if not strings:
        return None

    # Use the max function with the key argument set to len to find the longest string
    # The max function will return the first string with the maximum length in case of a tie
    return max(strings, key=len)


# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```