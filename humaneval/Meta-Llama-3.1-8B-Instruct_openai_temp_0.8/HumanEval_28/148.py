```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string

    Args:
        strings (List[str]): A list of strings to be concatenated

    Returns:
        str: The concatenated string

    Example:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)

# Example usage:
strings_list = []
print(concatenate(strings_list))  # Output: ''

strings_list = ['a', 'b', 'c']
print(concatenate(strings_list))  # Output: 'abc'
```

In this script, the `concatenate` function uses Python's built-in `join` method to concatenate the list of strings into a single string. The `join` method concatenates all the strings in the list into a single string, with the string it's called on (in this case, an empty string) separating each string. This means that the result is equivalent to calling the `+` operator on all the strings in the list, but is likely to be more efficient and concise.