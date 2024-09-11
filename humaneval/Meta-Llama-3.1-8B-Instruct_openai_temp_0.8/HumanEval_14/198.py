```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes in the string.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    prefixes = []
    for length in range(1, len(string) + 1):
        prefixes.append(string[:length])
    return prefixes

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
print(all_prefixes('a'))  # Output: ['a']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes from shortest to longest. It does this by iterating over the range of possible prefix lengths (from 1 to the length of the string), and for each length, it appends the corresponding prefix to the list. Finally, it returns the list of prefixes.