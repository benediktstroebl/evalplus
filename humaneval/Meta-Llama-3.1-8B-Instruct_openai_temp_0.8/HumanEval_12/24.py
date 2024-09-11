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
    # Check if the list is empty
    if not strings:
        return None

    # Use the max function with the key argument set to len to find the longest string
    # The max function in Python is stable, so in case of a tie, it will return the first element
    return max(strings, key=len)

# Test cases
print(longest([]))  # Should print: None

print(longest(['a', 'b', 'c']))  # Should print: 'a'

print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

In this script, we first check if the input list `strings` is empty. If it is, we return `None` as per the problem statement.

If the list is not empty, we use the `max` function to find the longest string. We pass `strings` as the first argument to `max`, and `len` as the `key` argument. This tells `max` to use the length of each string as the comparison key, so it returns the string with the maximum length.

The `max` function in Python is stable, meaning that in case of a tie (i.e., multiple strings of the same maximum length), it will return the first element. This is why we get the first string in case of multiple strings of the same length.