```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = [string[:i] for i in range(1, len(string) + 1)]
    return prefixes

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that generates all prefixes of a given string. The function uses a list comprehension to generate all prefixes by slicing the input string from index 1 to the current length (inclusive). The resulting prefixes are then returned as a list. The example usage demonstrates how to call the function with different input strings.