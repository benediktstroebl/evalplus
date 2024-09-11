```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string or None if the input list is empty.
    """
    if not strings:
        # If the input list is empty, return None.
        return None

    # Initialize the longest string as the first string in the list.
    longest_str = strings[0]

    # Iterate over the rest of the strings in the list.
    for string in strings[1:]:
        # If the length of the current string is greater than the length of the longest string,
        # update the longest string.
        if len(string) > len(longest_str):
            longest_str = string

    # Return the longest string.
    return longest_str


# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

Alternatively, you can use the built-in `max` function with a custom key function to make the code more concise:

```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string or None if the input list is empty.
    """
    return max(strings, key=len, default=None)


# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```