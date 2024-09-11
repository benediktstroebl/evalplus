```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return a list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of prefixes.

    Examples:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

In this script, a list comprehension is used to generate all prefixes of the input string. The `range(len(string))` generates indices from 0 to the length of the string minus 1. For each index `i`, `string[:i+1]` generates the prefix of length `i+1`. The result is a list of all prefixes from shortest to longest.