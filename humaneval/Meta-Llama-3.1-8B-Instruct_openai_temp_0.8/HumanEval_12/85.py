```markdown
### Longest String in a List
#### A Python function to find the longest string in a list, returning the first one in case of multiple strings of the same length

```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    Args:
    strings (List[str]): A list of strings

    Returns:
    Optional[str]: The longest string, or None if the input list is empty
    """
    # Check if the list is empty
    if not strings:
        return None

    # Use the built-in max function with a key to find the longest string
    # The key is a function that takes a string and returns its length
    # The max function will return the first string in case of a tie
    return max(strings, key=len)

# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```