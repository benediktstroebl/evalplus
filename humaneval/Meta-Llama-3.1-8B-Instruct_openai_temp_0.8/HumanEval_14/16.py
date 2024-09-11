```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.
    
    Args:
        string (str): The input string.
    
    Returns:
        List[str]: A list of all prefixes in order from shortest to longest.
    
    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(len(string)):
        prefixes.append(string[:i+1])
    return prefixes


# Test the function
print(all_prefixes('abc'))
```

This script defines a function `all_prefixes` that generates all prefixes of the input string. The function works by iterating over the length of the string and appending each prefix to the result list. The `[:i+1]` syntax is used to extract the prefix up to the current index `i`, inclusive. The function returns the list of prefixes.

When you run this script, it will print `['a', 'ab', 'abc']`, demonstrating that the function correctly generates all prefixes of the input string 'abc' in order from shortest to longest.