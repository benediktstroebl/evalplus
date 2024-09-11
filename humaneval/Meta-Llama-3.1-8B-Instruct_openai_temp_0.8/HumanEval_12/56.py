```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    
    Args:
        strings (List[str]): A list of strings.
    
    Returns:
        Optional[str]: The longest string in the list, or the first longest string if there are multiple,
        or None if the list is empty.
    """
    
    # Check if the input list is empty
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


# Test cases
if __name__ == "__main__":
    assert longest([]) is None
    assert longest(['a', 'b', 'c']) == 'a'
    assert longest(['a', 'bb', 'ccc']) == 'ccc'
```

This script defines the function `longest` that takes a list of strings as input and returns the longest string. If there are multiple strings of the same length, it returns the first one. If the input list is empty, it returns `None`. The script also includes test cases to verify the correctness of the function.