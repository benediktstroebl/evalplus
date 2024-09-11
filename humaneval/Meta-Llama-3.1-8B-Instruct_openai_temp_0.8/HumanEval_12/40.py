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
    if not strings:  # check if the list is empty
        return None

    longest_str = max(strings, key=len)  # find the longest string
    return longest_str  # return the longest string


# Test the function
if __name__ == "__main__":
    print(longest([]))  # should print None

    print(longest(['a', 'b', 'c']))  # should print 'a'
    print(longest(['a', 'bb', 'ccc']))  # should print 'ccc'
```

This script defines the `longest` function as specified and adds some test cases at the end to ensure the function works as expected. The `max` function with `key=len` is used to find the longest string in the list. This is a more concise and efficient way to solve the problem than checking each string's length manually.