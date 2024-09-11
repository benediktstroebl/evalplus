```markdown
### Longest String in a List
#### Problem Description
Out of a list of strings, return the longest one. 
Return the first one in case of multiple strings of the same length. 
Return None in case the input list is empty.

#### Solution

```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Return the longest string from a list of strings.
    
    If there are multiple strings of the same length, return the first one.
    If the input list is empty, return None.
    
    Args:
        strings (List[str]): A list of strings.
    
    Returns:
        Optional[str]: The longest string, or None if the input list is empty.
    """
    if not strings:  # check if the input list is empty
        return None
    
    return max(strings, key=len)  # return the longest string

# Example use cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
print(longest(['hello', 'apple', 'banana']))  # 'banana'
```

### How it Works
1. We first check if the input list `strings` is empty. If it is, we return `None`.
2. Otherwise, we use the built-in `max` function with a custom key function `len` to find the longest string in the list.
   The `max` function returns the first item in the list when there are multiple items with the same maximum value, which is exactly what we want.
3. The longest string is then returned by the function.