```markdown
### Problem: Generate All Prefixes of a String

This script generates all prefixes of a given string, from shortest to longest.
```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Example usage:
print(all_prefixes('abc'))
```

### Explanation

This script uses a list comprehension to generate all prefixes of the input string. It iterates over the indices of the string, slicing the string from the start to each index plus one (to include the character at the current index). The resulting prefixes are collected in a list and returned.

### Output

When run with the input `'abc'`, this script will output `['a', 'ab', 'abc']`.