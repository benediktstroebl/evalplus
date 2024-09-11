```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings

    Returns:
        Optional[str]: The longest string, or None if the list is empty
    """
    if not strings:  # Check if the list is empty
        return None

    longest_str = strings[0]  # Initialize the longest string as the first string in the list
    for s in strings:
        if len(s) > len(longest_str):  # Check if the current string is longer than the longest string
            longest_str = s  # Update the longest string

    return longest_str

# Example use cases:
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```