```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: A single string resulting from the concatenation.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Use the join() function to concatenate all strings in the list
    # The join() function takes an iterable of strings and concatenates them with the string it's called on
    # In this case, we call it on an empty string, so the strings are concatenated without any separator
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Should print: ''
print(concatenate(['a', 'b', 'c']))  # Should print: 'abc'
```

This script defines a function `concatenate()` that takes a list of strings and returns a single string by concatenating them all together. It uses the `join()` function to achieve this, which is a built-in method in Python that is efficient and concise for this purpose. The script also includes docstrings and test cases to demonstrate its usage.