Here's a Python script that implements the `longest` function:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one.
    Return the first one in case of multiple strings of the same length.
    Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string in the list, or None if the list is empty.
    """
    if not strings:  # Check if the list is empty
        return None

    # Use the max function with a custom key to find the longest string
    # The key is a lambda function that returns the length of each string
    return max(strings, key=len)


# Example usage:
print(longest([]))  # Should print None
print(longest(['a', 'b', 'c']))  # Should print 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print 'ccc'
```
In this script, we use the built-in `max` function to find the longest string in the list. We pass a custom key function to `max`, which is a lambda function that returns the length of each string. This allows `max` to compare the strings based on their lengths.

Note that the `key` argument is a really powerful feature of the `max` function, and it allows you to define a custom comparison function for the values being compared. In this case, we use it to compare the strings based on their lengths, but you can use it to compare values based on any criteria you need.