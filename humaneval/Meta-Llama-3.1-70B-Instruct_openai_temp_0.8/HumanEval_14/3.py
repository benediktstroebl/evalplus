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

This script uses list comprehension to generate all prefixes of the input string. The expression `string[:i+1]` generates a substring from the start of the string up to the `i-th` character, and this is done for all characters in the string. The result is a list of all prefixes of the input string, from shortest to longest.