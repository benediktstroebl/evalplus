```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.

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

This script defines a function `all_prefixes` that takes a string as an input and returns a list of all its prefixes from shortest to longest. The function uses a loop to generate each prefix by slicing the input string up to the current position `i` and appends it to the list of prefixes. Finally, it returns the list of prefixes. The script also includes a test case to demonstrate the function's behavior.