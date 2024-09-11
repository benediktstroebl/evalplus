```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the longest string from a given list of strings.
    
    If there are multiple strings of the same maximum length, 
    returns the first one encountered.
    
    Returns None if the input list is empty.
    
    :param strings: A list of strings
    :return: The longest string or None
    """
    if not strings:  # Check if the list is empty
        return None
    
    return max(strings, key=len)  # Use the built-in max function with len as the key


# Example usage:
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```