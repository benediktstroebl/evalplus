```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
    string (str): The input string

    Returns:
    List[str]: A list of all prefixes in the input string, from shortest to longest

    Example:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefix = string[:i]
        prefixes.append(prefix)
    return prefixes

# Test the function
print(all_prefixes('abc'))
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the string, from shortest to longest. It does this by iterating over the range of indices from 1 to the length of the string (inclusive), and for each index `i`, it gets the prefix of the string up to index `i` using string slicing (`string[:i]`). It then appends this prefix to the list of prefixes. Finally, it returns the list of prefixes.