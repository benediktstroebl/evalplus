```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes from shortest to longest.

    Examples:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all its prefixes, from the shortest to the longest. It uses a list comprehension to generate the prefixes, iterating over the indices of the characters in the string and slicing the string up to each index. The result is a list of all prefixes, which is then returned. The example usage at the end demonstrates how to use the function and what output to expect.