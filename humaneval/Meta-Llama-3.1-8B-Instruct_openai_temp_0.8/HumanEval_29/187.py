```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    
    Args:
        strings (List[str]): The list of input strings.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: A list of strings that start with the given prefix.

    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]

# Example usage:
strings = ['abc', 'bcd', 'cde', 'array', 'xyz', 'abx']
prefix = 'ab'
print(filter_by_prefix(strings, prefix))  # Output: ['abc', 'abx']
```

In this script, I've implemented the `filter_by_prefix` function using a list comprehension. This function takes a list of strings and a prefix as input, and returns a new list containing only the strings that start with the given prefix. The `startswith` method is used to check if a string starts with the given prefix.