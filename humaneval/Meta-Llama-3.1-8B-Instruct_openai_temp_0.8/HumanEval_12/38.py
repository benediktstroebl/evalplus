```markdown
### Longest String in a List
#### Solution in Python

```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    
    Args:
    strings (List[str]): A list of strings.
    
    Returns:
    Optional[str]: The longest string in the list, or None if the list is empty.
    """
    
    # Check if the list is empty
    if not strings:
        return None
    
    # Initialize the longest string as the first one in the list
    longest_str = strings[0]
    
    # Iterate over the list to find the longest string
    for string in strings:
        if len(string) > len(longest_str):
            longest_str = string
    
    return longest_str

# Example use cases
print(longest([]))  # Should return None
print(longest(['a', 'b', 'c']))  # Should return 'a'
print(longest(['a', 'bb', 'ccc']))  # Should return 'ccc'
```
This script defines a function `longest` that takes a list of strings as input and returns the longest string. If the input list is empty, it returns `None`. If there are multiple strings of the same maximum length, it returns the first one it encounters.