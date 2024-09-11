```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of prefixes in order from shortest to longest.

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
print(all_prefixes('def'))  # Output: ['d', 'de', 'def']
print(all_prefixes('xyz'))  # Output: ['x', 'xy', 'xyz']
```

In this script, we use a for loop to generate all prefixes of the input string by slicing the string with different start and end indices. The `range(1, len(string) + 1)` generates indices from 1 to the length of the string, and `string[:i]` gets the substring from the start of the string to the `i-th` character. The prefixes are then appended to a list, which is returned at the end.