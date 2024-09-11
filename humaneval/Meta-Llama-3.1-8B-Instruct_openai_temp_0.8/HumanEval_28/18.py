```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
        strings (List[str]): A list of strings to be concatenated

    Returns:
        str: A single string that is the concatenation of all input strings

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Use the join() method to concatenate all strings in the list
    # The join() method returns a string in which the elements of the list have been joined by the string on which the method was called
    # Since we want strings joined without any separator, we use an empty string
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```

This script defines a function `concatenate` that takes a list of strings as input and returns a single string that is the concatenation of all input strings. The function uses the `join()` method to concatenate the strings, and the `print()` function is used to test the function with some examples.