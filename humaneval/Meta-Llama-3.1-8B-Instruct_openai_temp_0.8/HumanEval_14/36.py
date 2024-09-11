```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes from shortest to longest.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Example usage
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes from shortest to longest. The function uses a list comprehension to generate the prefixes. It iterates over the indices of the input string, slicing the string from the start up to and including each index. The resulting prefixes are returned as a list.

In the example usage, we call `all_prefixes` with the string `'abc'` and print the result, which is `['a', 'ab', 'abc']`.