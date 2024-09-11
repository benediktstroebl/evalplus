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
    
    # Check if the input list is empty
    if not strings:
        return None  # Return None if the list is empty

    # Initialize the longest string as the first one in the list
    longest_str = strings[0]

    # Iterate over the rest of the list
    for s in strings[1:]:
        # If the current string is longer than the longest string found so far
        if len(s) > len(longest_str):
            longest_str = s  # Update the longest string

    return longest_str  # Return the longest string


# Test cases
if __name__ == "__main__":
    print(longest([]))  # Should print: None

    print(longest(['a', 'b', 'c']))  # Should print: 'a'

    print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script first checks if the input list is empty. If it is, it returns `None`. Otherwise, it initializes the longest string as the first one in the list. It then iterates over the rest of the list, updating the longest string whenever it finds a longer one. Finally, it returns the longest string found. The test cases at the end verify that the function behaves correctly.