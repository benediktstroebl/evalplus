```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
        strings (List[str]): A list of strings to concatenate

    Returns:
        str: A single string concatenated from the input list

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Using the join method to concatenate all strings in the list
    return ''.join(strings)

# Test cases
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```

This script defines a function `concatenate` that takes a list of strings as input and returns a single string that is the concatenation of all strings in the input list. It uses the `join` method of the empty string `''`, which concatenates all the strings in the list without any separator. The script also includes test cases to demonstrate the function's behavior.