```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes in the input string.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        # Get the substring from the start of the string to the current index
        prefix = string[:i]
        prefixes.append(prefix)
    return prefixes

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the string. The function uses a loop to generate all prefixes by slicing the input string from the start to each index from 1 to the length of the string. The prefixes are then returned as a list. The example use cases are provided to demonstrate how to use the function.