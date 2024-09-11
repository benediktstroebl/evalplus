```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string in the list, or None if the list is empty.
    """
    # Check if the list is empty
    if not strings:
        return None

    # Use the max function with a key argument to find the longest string
    # The key argument specifies that we want to compare the strings based on their length
    # The max function will return the first string it encounters with the maximum length
    return max(strings, key=len)


# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

This script uses the built-in `max` function in Python, which returns the largest item in an iterable or the largest of two or more arguments. The `key` argument of the `max` function is a function that takes a list element and returns a value that will be used for comparison purposes. In this case, the `key` function is `len`, which returns the length of a string. This means that `max` will return the string with the maximum length. If there are multiple strings with the same maximum length, `max` will return the first one it encounters.