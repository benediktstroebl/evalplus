### Longest String from a List
#### Problem Statement
Find the longest string from a given list of strings. If there are multiple strings of the same maximum length, return the first one. If the input list is empty, return `None`.

#### Solution
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
    # Check if the list is empty
    if not strings:
        return None
    
    # Initialize the longest string as the first string in the list
    longest_str = strings[0]
    
    # Iterate over the list of strings
    for s in strings:
        # If the current string is longer than the longest string found so far, update the longest string
        if len(s) > len(longest_str):
            longest_str = s
    
    # Return the longest string
    return longest_str

# Example usage:
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

#### Note
This solution iterates over the list of strings only once, making it efficient for large lists. The time complexity is O(n), where n is the number of strings in the list.