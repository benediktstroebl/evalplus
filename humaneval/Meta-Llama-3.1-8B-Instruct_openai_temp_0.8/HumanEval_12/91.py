```markdown
### Solution: Longest String in List

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
    if not strings:  # Check if the list is empty
        return None  # Return None if the list is empty
    
    longest_str = strings[0]  # Initialize longest string as the first string in the list
    max_length = len(longest_str)  # Initialize max length as the length of the first string
    
    for string in strings:  # Iterate over the list of strings
        if len(string) > max_length:  # Check if the current string is longer than the max length
            longest_str = string  # Update longest string
            max_length = len(string)  # Update max length
    
    return longest_str  # Return the longest string

# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script uses a simple iteration to find the longest string in the list. If the list is empty, it returns `None`. If there are multiple strings of the same maximum length, it returns the first one it encounters.