```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
        strings (List[str]): A list of strings to be concatenated

    Returns:
        str: A single string that is the concatenation of all the strings in the input list

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)


# Test the function
if __name__ == "__main__":
    print(concatenate([]))  # Output: ''
    print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```

This script defines a function `concatenate` that takes a list of strings as input and returns a single string that is the concatenation of all the strings in the input list. The function uses the `join` method of the empty string to concatenate the list of strings. The test code at the end of the script checks that the function behaves correctly for both an empty list and a non-empty list of strings.