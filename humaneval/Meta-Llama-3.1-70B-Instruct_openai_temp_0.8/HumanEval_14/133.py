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

This script uses a list comprehension to generate all prefixes of the input string. The expression `string[:i+1]` generates a prefix of length `i+1` by slicing the string from the beginning to the `i+1`th character. The `range(len(string))` generates indices from 0 to the length of the string minus one, so `i+1` ranges from 1 to the length of the string.