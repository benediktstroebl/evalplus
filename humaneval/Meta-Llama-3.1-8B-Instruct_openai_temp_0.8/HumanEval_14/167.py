```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string, from shortest to longest.

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

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the string, from shortest to longest. The function uses a loop to generate all prefixes by slicing the input string from index 0 to the current index `i`, and then returns the list of prefixes. The test case at the end demonstrates how to use the function.