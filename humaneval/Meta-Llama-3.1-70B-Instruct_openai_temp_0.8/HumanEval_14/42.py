```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
    string (str): The input string.

    Returns:
    List[str]: A list of all prefixes from shortest to longest.

    Examples:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines the function `all_prefixes` which takes a string as input and returns a list of all prefixes from shortest to longest. It uses list comprehension to generate the prefixes by slicing the input string from the start up to each index from 1 to the length of the string. The function includes a docstring that explains its purpose, parameters, return value, and provides an example usage.