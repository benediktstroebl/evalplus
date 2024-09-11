```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string in the list or None if the list is empty.
    """
    if not strings:  # Check if the input list is empty
        return None

    # Use the max function with a key argument to find the longest string
    # The max function returns the first maximum element in case of a tie
    return max(strings, key=len)


# Test cases
if __name__ == "__main__":
    print(longest([]))  # Should print: None
    print(longest(['a', 'b', 'c']))  # Should print: 'a'
    print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script defines a function `longest` that takes a list of strings and returns the longest one. If there are multiple strings of the same length, it returns the first one. If the input list is empty, it returns `None`. The test cases demonstrate the function's behavior.