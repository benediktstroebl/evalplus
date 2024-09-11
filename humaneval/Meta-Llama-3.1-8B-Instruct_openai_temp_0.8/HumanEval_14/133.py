```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return a list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    prefixes = [string[i:] for i in range(len(string) + 1)]
    return prefixes

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script uses list comprehension to generate all prefixes of the input string. The expression `string[i:]` generates a substring of `string` starting from index `i` to the end of the string. This is equivalent to getting all prefixes of `string`. The outer list comprehension then generates all such substrings for all indices `i` from 0 to the length of `string`-1 (inclusive), resulting in all prefixes of `string` in order from shortest to longest.