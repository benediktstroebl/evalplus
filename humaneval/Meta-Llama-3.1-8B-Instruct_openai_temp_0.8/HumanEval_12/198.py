```markdown
### Longest String in a List
#### Python Script

This script takes a list of strings as input and returns the longest string. In case of multiple strings of the same length, it returns the first one. If the input list is empty, it returns None.

```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
    strings (List[str]): A list of strings

    Returns:
    Optional[str]: The longest string in the list, or None if the list is empty
    """
    if not strings:  # Check if the list is empty
        return None

    longest_str = strings[0]  # Initialize the longest string as the first one in the list
    for string in strings:  # Iterate over the list of strings
        if len(string) > len(longest_str):  # Check if the current string is longer
            longest_str = string  # Update the longest string

    return longest_str  # Return the longest string

# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string. It first checks if the list is empty and returns None in that case. Then, it iterates over the list of strings, keeping track of the longest string encountered so far. Finally, it returns the longest string. The test cases at the end of the script verify that the function works as expected.