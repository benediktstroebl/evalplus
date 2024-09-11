```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return a list of all prefixes from shortest to longest of the input string.

    Args:
    string (str): The input string.

    Returns:
    List[str]: A list of all prefixes from shortest to longest.

    Example:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]


# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```
This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes from shortest to longest. The function uses a list comprehension to generate the prefixes. The `string[:i+1]` expression generates each prefix by slicing the input string up to the `i+1` index, where `i` ranges from 0 to the length of the string minus 1. The example usage at the end demonstrates how to use the function.