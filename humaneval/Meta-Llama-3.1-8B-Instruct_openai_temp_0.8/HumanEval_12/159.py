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
    if not strings:
        # If the list is empty, return None
        return None
    
    longest_str = strings[0]
    # Initialize the longest string as the first string in the list
    
    for s in strings[1:]:
        # Iterate over the rest of the strings in the list
        if len(s) > len(longest_str):
            # If a longer string is found, update the longest string
            longest_str = s
    
    return longest_str
```

You can test the function with the example use cases you provided:

```python
print(longest([]))  # Should print None
print(longest(['a', 'b', 'c']))  # Should print 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print 'ccc'
```