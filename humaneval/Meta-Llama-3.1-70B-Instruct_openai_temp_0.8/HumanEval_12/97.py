```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string in the list, or None if the list is empty.
    """
    if not strings:  # Check if the input list is empty
        return None
    return max(strings, key=len)  # Use the max function with len as the key

# Test cases
print(longest([]))  # Should return None
print(longest(['a', 'b', 'c']))  # Should return 'a'
print(longest(['a', 'bb', 'ccc']))  # Should return 'ccc'
```

This script uses the built-in `max` function in Python, which returns the largest item in an iterable or the largest of two or more arguments. The `key` argument specifies a function of one argument that is used to extract a comparison key from each element in the list. In this case, we use `len` as the key, which means the `max` function will return the longest string in the list. If the list is empty, the `max` function will raise a `ValueError`, but we catch this case by checking if the list is empty before calling `max`.