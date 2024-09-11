```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.
    
    Args:
        strings (List[str]): A list of strings.
    
    Returns:
        Optional[str]: The longest string in the list or None if the list is empty.
    """
    
    # Check if the list is empty
    if not strings:
        return None
    
    # Initialize the longest string with the first one in the list
    longest_str = strings[0]
    
    # Iterate over the rest of the list
    for s in strings[1:]:
        # If the current string is longer than the current longest string, update the longest string
        if len(s) > len(longest_str):
            longest_str = s
    
    # Return the longest string
    return longest_str


# Test the function
if __name__ == "__main__":
    print(longest([]))  # None
    print(longest(['a', 'b', 'c']))  # 'a'
    print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

This script defines a function `longest` that takes a list of strings and returns the longest one. If the list is empty, it returns `None`. If there are multiple strings of the same length, it returns the first one. The script also includes test cases to verify the function's behavior.