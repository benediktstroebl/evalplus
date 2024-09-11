```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Returns a list of all prefixes from shortest to longest of the input string.

    Args:
    string (str): The input string for which prefixes are generated.

    Returns:
    List[str]: A list of prefixes from shortest to longest.
    """
    return [string[:i+1] for i in range(len(string))]

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

In this script, we use list comprehension to generate all prefixes of the input string. The expression `string[:i+1]` generates the prefix of length `i+1` for each `i` in the range from 0 to `len(string) - 1`.