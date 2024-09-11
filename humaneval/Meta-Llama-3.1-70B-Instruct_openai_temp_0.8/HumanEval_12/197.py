```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the longest string in a list of strings.
    
    If there are multiple strings with the same maximum length, returns the first one.
    Returns None if the input list is empty.
    
    :param strings: A list of strings
    :return: The longest string or None
    """
    
    # Check if the input list is empty
    if not strings:
        return None

    # Initialize the longest string with the first string in the list
    longest_str = strings[0]

    # Iterate over the rest of the strings in the list
    for string in strings[1:]:
        # If the current string is longer than the longest string found so far, update the longest string
        if len(string) > len(longest_str):
            longest_str = string

    # Return the longest string
    return longest_str


# Example usage:
print(longest([]))  # Expected output: None
print(longest(['a', 'b', 'c']))  # Expected output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Expected output: 'ccc'
```

Alternatively, you can use the built-in `max` function with a custom key to achieve the same result in a more concise way:

```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the longest string in a list of strings.
    
    If there are multiple strings with the same maximum length, returns the first one.
    Returns None if the input list is empty.
    
    :param strings: A list of strings
    :return: The longest string or None
    """
    
    # Check if the input list is empty
    if not strings:
        return None

    # Use the max function with a custom key to find the longest string
    return max(strings, key=len)


# Example usage:
print(longest([]))  # Expected output: None
print(longest(['a', 'b', 'c']))  # Expected output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Expected output: 'ccc'
```

However, note that the `max` function will return the last string in case of multiple strings with the same maximum length, whereas the original implementation returns the first one. If you want to preserve the original behavior, you can use a custom function like the first example.