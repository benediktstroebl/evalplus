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
        prefixes.append(string[:i])
    return prefixes


# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the string, from shortest to longest. It uses a loop to generate each prefix by slicing the input string up to the current index. The example usage shows how to call the function with different inputs.