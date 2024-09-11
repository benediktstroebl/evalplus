```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.
    """
    return [string[:i+1] for i in range(len(string))]

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines the function `all_prefixes` that uses a list comprehension to generate all prefixes of the input string. The `range(len(string))` generates indices from 0 to the length of the string minus 1. The `string[:i+1]` slices the string up to the current index plus 1, effectively creating a prefix. The resulting list of prefixes is then returned by the function.