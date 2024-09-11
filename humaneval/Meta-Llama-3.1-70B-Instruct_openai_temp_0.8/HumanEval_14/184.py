```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that takes an input string and returns a list of all its prefixes, from the shortest to the longest. The function uses a list comprehension to generate the prefixes by slicing the input string at each position from 0 to the length of the string. The `[:i+1]` slice means "from the start of the string up to but not including the character at position `i+1`".