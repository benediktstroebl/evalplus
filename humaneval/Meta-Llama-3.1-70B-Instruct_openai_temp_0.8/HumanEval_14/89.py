```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.

    Examples:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Example usage
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that generates all prefixes of a given string. The function uses a list comprehension to create a list of substrings, where each substring starts at the beginning of the input string and ends at each position from 1 to the length of the string. The result is a list of all prefixes of the input string, from shortest to longest.