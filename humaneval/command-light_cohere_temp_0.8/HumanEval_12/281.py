```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """ Returns the longest string from a list of strings.
    Args:
    strings (List[str]): List of strings
    Returns:
    str: The longest string
    None: If the list is empty
    """
    if not strings:
        return None
    return max(strings, key=len)

# Example usage:
strings = ['a', 'b', 'c', 'bb', 'ccc']
longest_result = longest(strings)
print(longest_result)  # Output: 'ccc'
```

In this code, we have defined a function called **longest** that takes a list of strings as input and returns the longest string from that list. It uses the **max** function with a custom key function (set to **len**) to identify the longest string in the list.