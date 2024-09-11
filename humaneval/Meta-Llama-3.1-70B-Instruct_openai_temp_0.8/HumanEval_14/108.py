```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]

# Example usage
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that uses a list comprehension to generate all prefixes of the input string. The list comprehension iterates over the range from 1 to the length of the string (inclusive), slicing the string up to the current index `i` in each iteration. The result is a list of all prefixes from shortest to longest.