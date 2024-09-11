```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
    string (str): The input string

    Returns:
    List[str]: A list of all prefixes from shortest to longest

    Example:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Example usage
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines the `all_prefixes` function which generates all prefixes of the input string. The list comprehension `[string[:i+1] for i in range(len(string))]` iterates over the indices of the input string, slicing the string to get each prefix. The result is a list of all prefixes from shortest to longest.