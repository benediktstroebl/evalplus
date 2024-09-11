```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
        strings (List[str]): A list of strings to be concatenated

    Returns:
        str: The concatenated string
    """
    # Use the join() method to concatenate all strings in the list
    # The join() method requires an iterable of strings, so we can use the list directly
    # The empty string is used as the separator, effectively concatenating the strings without any separation
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```

In this script, we use the `join()` method of Python's string class to concatenate the strings in the list. The `join()` method returns a string in which the elements of the iterable (in this case, the list of strings) have been joined by the string on which the method was called (in this case, an empty string). This effectively concatenates the strings without any separation.