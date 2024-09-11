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

    # Check if the input list is empty
    if not strings:
        return None

    # Initialize the longest string with the first string in the list
    longest_str = strings[0]

    # Iterate over the list of strings starting from the second string
    for string in strings[1:]:
        # Check if the current string is longer than the longest string found so far
        if len(string) > len(longest_str):
            # Update the longest string
            longest_str = string

    # Return the longest string
    return longest_str


# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

Alternatively, you can use the built-in `max` function with a key argument to achieve the same result in a more concise way:

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

    # Check if the input list is empty
    if not strings:
        return None

    # Use the max function with a key argument to find the longest string
    return max(strings, key=len)


# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```