### Longest String in a List
#### Problem Description
Given a list of strings, return the longest string. In case of a tie, return the first string. If the input list is empty, return `None`.

#### Code
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
    if not strings:  # If the list is empty, return None
        return None
    return max(strings, key=len)  # Return the longest string

# Example use cases
if __name__ == "__main__":
    print(longest([]))  # Should print: None
    print(longest(['a', 'b', 'c']))  # Should print: 'a'
    print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```
#### Explanation
This script defines a function `longest` that takes a list of strings and returns the longest string. It uses the built-in `max` function with the `key` argument set to `len` to find the longest string. If the input list is empty, it returns `None`. The example use cases demonstrate the function's behavior with different inputs.