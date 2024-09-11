```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    
    Args:
        strings (List[str]): A list of strings.
    
    Returns:
        Optional[str]: The longest string in the list or None if the list is empty.
    """
    if not strings:
        # If the list is empty, return None
        return None
    
    # Use the max function with a custom key to find the longest string
    # The key function returns the length of each string
    # The max function returns the first item with the maximum length
    return max(strings, key=len)


# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```