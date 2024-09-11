### Longest String in a List

This Python script defines a function `longest` that takes a list of strings as input and returns the longest string. If there are multiple strings of the same maximum length, it returns the first one encountered. If the input list is empty, it returns `None`.

```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.
    
    Args:
    strings (List[str]): A list of strings.
    
    Returns:
    Optional[str]: The longest string in the input list or None if the list is empty.
    """
    
    # Check if the list is empty
    if not strings:
        return None
    
    # Initialize the longest string as the first string in the list
    longest_str = strings[0]
    
    # Iterate over the list of strings
    for s in strings:
        # If a string is longer than the current longest string, update the longest string
        if len(s) > len(longest_str):
            longest_str = s
    
    # Return the longest string
    return longest_str

# Test cases
if __name__ == "__main__":
    print(longest([]))  # Should print: None
    print(longest(['a', 'b', 'c']))  # Should print: a
    print(longest(['a', 'bb', 'ccc']))  # Should print: ccc
```

This script uses a simple iterative approach to find the longest string in the list. It initializes the longest string as the first string in the list and then iterates over the rest of the list, updating the longest string whenever it encounters a longer string. If the input list is empty, it returns `None`. The test cases at the end verify that the function behaves correctly in different scenarios.