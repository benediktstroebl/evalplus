```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Returns a list of all prefixes from shortest to longest of the input string.

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
        prefixes.append(string[:i])
    return prefixes

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
print(all_prefixes('xyz'))  # Output: ['x', 'xy', 'xyz']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all its prefixes, from shortest to longest. It uses a for loop to generate all prefixes by slicing the string at each possible position. The prefixes are then returned as a list. The script also includes test cases to demonstrate the function's behavior.