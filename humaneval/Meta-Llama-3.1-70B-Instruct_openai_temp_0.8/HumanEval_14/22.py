```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return a list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of prefixes.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i + 1] for i in range(len(string))]


# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script uses a list comprehension to generate the prefixes. It iterates over the indices of the input string, slicing the string up to each index plus one to include the current character in the prefix. The resulting prefixes are collected in a list, which is then returned.