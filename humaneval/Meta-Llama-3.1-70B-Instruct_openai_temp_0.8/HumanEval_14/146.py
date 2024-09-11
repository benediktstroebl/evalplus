```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Returns a list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of prefixes.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]


# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that takes an input string and returns a list of all prefixes from shortest to longest. It uses a list comprehension to generate the prefixes. The `[:i+1]` slice generates all characters in the string up to and including the `i-th` character. The `range(len(string))` generates indices for all characters in the string. The test at the end of the script demonstrates how the function works.