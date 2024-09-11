### Prefix Generator Script
```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
    string (str): The input string.

    Returns:
    List[str]: A list of prefixes.

    Example:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```
This script defines a function `all_prefixes` that generates all prefixes of a given string. It does this by iterating over the length of the string, and at each step, it appends a substring of the string up to that length to a list of prefixes. The function then returns this list of prefixes. The script also includes a test to demonstrate the function's behavior.