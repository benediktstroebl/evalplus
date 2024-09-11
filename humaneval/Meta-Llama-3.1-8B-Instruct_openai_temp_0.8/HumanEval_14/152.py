```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Parameters:
    string (str): The input string.

    Returns:
    List[str]: A list of prefixes in order from shortest to longest.

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes


# Example usage
print(all_prefixes('abc'))
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all its prefixes in order from shortest to longest. The function uses a for loop to generate all prefixes by slicing the string from the first character to each subsequent position. The example usage at the end demonstrates how to call this function with the input string `'abc'`.