```markdown
### Longest String in a List
#### Problem Description
Given a list of strings, return the longest string. In case of multiple strings of the same length, return the first one. If the input list is empty, return None.

#### Solution
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Return the longest string in a list of strings. 
    In case of multiple strings of the same length, return the first one. 
    Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string in the input list, or None if the list is empty.
    """
    # Check if the input list is empty
    if not strings:
        return None
    
    # Use the max function with a key argument to find the longest string
    # The key argument specifies that we want to compare the strings based on their lengths
    return max(strings, key=len)
```

#### Example Usage
```python
print(longest([]))  # Output: None
print(longest(['a', 'b', 'c']))  # Output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
```
```