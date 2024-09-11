```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script uses a list comprehension to generate all prefixes of the input string. The `string[:i]` expression slices the string up to the `i`-th character, and the `range(1, len(string) + 1)` generates indices from 1 to the length of the string (inclusive). The resulting list of prefixes is then returned by the `all_prefixes` function.