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
        Optional[str]: The longest string in the list or None if the list is empty.
    """
    # Filter out empty strings
    strings = [string for string in strings if string]

    # If the list is empty, return None
    if not strings:
        return None

    # Use the built-in max function with a key argument to find the longest string
    # The key argument tells max to use the length of each string as the comparison value
    return max(strings, key=len)

# Test cases
if __name__ == "__main__":
    # Test with an empty list
    assert longest([]) is None

    # Test with a list of three strings
    assert longest(['a', 'b', 'c']) == 'a'

    # Test with a list of strings of different lengths
    assert longest(['a', 'bb', 'ccc']) == 'ccc'
```

This script defines the `longest` function which takes a list of strings as input, filters out any empty strings, checks if the list is empty, and then uses the `max` function with a key argument to find the longest string. The `max` function is used with a key argument set to `len`, which causes it to compare the lengths of the strings instead of their lexicographical order. 

The script also includes test cases to verify that the function behaves correctly in different scenarios. The `if __name__ == "__main__":` block checks the function's behavior when the script is run directly (not imported as a module).