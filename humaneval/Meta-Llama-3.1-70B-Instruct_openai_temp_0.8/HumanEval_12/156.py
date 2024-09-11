```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string in the list, or None if the list is empty.
    """

    # Check if the input list is empty
    if not strings:
        return None

    # Use the max function with the key argument set to len to find the longest string
    # The max function will return the first string with the maximum length in case of multiple strings of the same length
    return max(strings, key=len)


# Test cases
print(longest([]))  # Should print None
print(longest(['a', 'b', 'c']))  # Should print 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print 'ccc'
```

Note: The `max` function in Python returns the largest item in an iterable or the largest of two or more arguments. When used with the `key` argument, it returns the item with the largest value of the key function. In this case, the key function is `len`, which returns the length of a string.