```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): Input string for which prefixes are to be generated

    Returns:
        List[str]: List of prefixes in order from shortest to longest

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that generates all prefixes of a given string. It iterates over the string, taking substrings of increasing length, and stores these prefixes in a list. The function then returns this list. The test at the end demonstrates the function's behavior.