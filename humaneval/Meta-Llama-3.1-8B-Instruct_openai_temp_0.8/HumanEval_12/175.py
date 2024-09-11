```markdown
### Python Script to Find the Longest String in a List

#### Code
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
        Optional[str]: The longest string in the list, or None if the list is empty
    """
    if not strings:
        return None
    return max(strings, key=len)


# Example Use Cases
if __name__ == "__main__":
    print(longest([]))  # Output: None
    print(longest(['a', 'b', 'c']))  # Output: 'a'
    print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
```

#### Explanation

This Python script defines a function `longest` that takes a list of strings as input and returns the longest string. If there are multiple strings of the same maximum length, it returns the first one. If the input list is empty, it returns `None`.

The function uses the built-in `max` function with the `key` argument set to `len`, which tells `max` to compare the lengths of the strings instead of their lexicographical order.

The example use cases demonstrate the behavior of the function in different scenarios.