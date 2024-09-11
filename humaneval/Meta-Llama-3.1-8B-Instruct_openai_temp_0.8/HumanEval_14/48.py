```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string

    Returns:
        List[str]: List of all prefixes of the input string

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes

# Test the function
print(all_prefixes('abc'))
```

This script uses a `for` loop to generate all prefixes of the input string by slicing the string from index `0` to `i`, where `i` ranges from `1` to the length of the string. The generated prefixes are then stored in the `prefixes` list and returned by the function.