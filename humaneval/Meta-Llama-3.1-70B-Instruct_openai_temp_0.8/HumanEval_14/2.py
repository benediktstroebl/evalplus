```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
    string (str): The input string.

    Returns:
    List[str]: A list of all prefixes.

    Example:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script uses a list comprehension to generate all prefixes of the input string. It does this by slicing the string from the start up to each index `i+1`, where `i` ranges from 0 to the length of the string minus 1. The `[:i+1]` slice means "start at the beginning of the string and go up to, but not including, the `i+1`th character".