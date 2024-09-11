Here's the Python script that solves the problem:
```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
        strings (List[str]): A list of strings to be concatenated

    Returns:
        str: A single string that is the concatenation of all strings in the input list

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)

# Testing the function
if __name__ == "__main__":
    print(concatenate([]))  # Output: ''
    print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```
This script defines a function `concatenate` that takes a list of strings and returns a single string that is the concatenation of all strings in the input list. It uses the `join` method of the string `''.join(strings)` to concatenate the strings in the list. The `if __name__ == "__main__":` block is used to test the function when the script is run directly.