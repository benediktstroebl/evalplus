```markdown
### Longest String in a List
#### Problem Description
Given a list of strings, find the longest string and return it. If multiple strings have the same maximum length, return the first one. If the input list is empty, return `None`.

#### Solution
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
    Optional[str]: The longest string, or None if the input list is empty.
    """
    if not strings:  # Check if the input list is empty
        return None

    return max(strings, key=len)  # Return the longest string

# Test cases
if __name__ == "__main__":
    print(longest([]))  # None
    print(longest(['a', 'b', 'c']))  # 'a'
    print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

### Explanation
This script defines a function `longest` that takes a list of strings as input and returns the longest string. It uses the built-in `max` function with the `key` argument set to `len` to find the longest string. If the input list is empty, it returns `None`. The test cases at the end demonstrate the function's behavior with different inputs.