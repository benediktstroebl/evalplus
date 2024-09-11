```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: The concatenated string.
    """
    # Use the join() function to concatenate all strings in the list
    # The join() function takes an iterable as an argument and concatenates all its elements with the string it is called on
    # We call join() on an empty string, so all elements are concatenated without any separator
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```

This script defines a function `concatenate` that takes a list of strings and returns their concatenation as a single string. It uses the `join` method of the empty string `''` to concatenate all the strings in the list. The script also includes test cases to demonstrate the function's behavior.