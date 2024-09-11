```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of prefixes from shortest to longest.

    Examples:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]


# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script uses a list comprehension to generate all prefixes of the input string. The `string[:i+1]` expression generates a substring from the start of the string up to but not including the `i+1`th character. The `range(len(string))` expression generates indices from 0 up to but not including the length of the string.