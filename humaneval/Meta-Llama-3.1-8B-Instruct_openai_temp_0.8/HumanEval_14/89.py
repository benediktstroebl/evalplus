```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): Input string.

    Returns:
        List[str]: List of prefixes in the order from shortest to longest.

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

This script defines a function `all_prefixes` that generates all prefixes of a given string, ordered from shortest to longest. The function uses a loop to slice the input string from index 1 to the full length, appending each slice (prefix) to the `prefixes` list. Finally, the function returns the `prefixes` list. The code includes a test case to demonstrate the function's behavior.