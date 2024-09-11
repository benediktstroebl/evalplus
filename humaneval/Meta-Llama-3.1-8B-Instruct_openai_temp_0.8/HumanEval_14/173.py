```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of prefixes in the order from shortest to longest.

    Examples:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]


# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that generates all prefixes of a given string. It uses a list comprehension to create a list of prefixes by taking substrings of the input string from index 0 to the current index `i`, where `i` ranges from 1 to the length of the string. The `range(1, len(string) + 1)` part ensures that we get all prefixes, including the empty prefix (at index 0, but we start at index 1). The result is a list of all prefixes in the order from shortest to longest.