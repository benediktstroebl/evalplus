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
    Optional[str]: The longest string in the list, or None if the list is empty
    """
    if not strings:
        return None  # Return None if the list is empty
    
    # Initialize longest string with the first string in the list
    longest_str = strings[0]
    
    # Iterate over the list of strings
    for s in strings:
        # If the current string is longer than the longest string, update longest string
        if len(s) > len(longest_str):
            longest_str = s
    
    return longest_str

# Test cases
print(longest([]))  # Expected output: None

print(longest(['a', 'b', 'c']))  # Expected output: 'a'

print(longest(['a', 'bb', 'ccc']))  # Expected output: 'ccc'
```

However, we can improve this script by using Python's built-in functions and features. Here's a more concise version:

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
    Optional[str]: The longest string in the list, or None if the list is empty
    """
    return next((s for s in strings if len(s) == max(map(len, strings))), None)

# Test cases
print(longest([]))  # Expected output: None

print(longest(['a', 'b', 'c']))  # Expected output: 'a'

print(longest(['a', 'bb', 'ccc']))  # Expected output: 'ccc'
```
This version uses a generator expression with `next()` to find the first string with the maximum length, which is more concise and easier to read.