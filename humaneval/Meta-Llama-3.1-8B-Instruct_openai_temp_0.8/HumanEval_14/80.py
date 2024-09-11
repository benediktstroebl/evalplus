```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): Input string

    Returns:
        List[str]: List of all prefixes of the input string

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Test the function
print(all_prefixes('abc'))
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of that string, from the shortest to the longest. It uses a list comprehension to generate the prefixes by slicing the input string at each position from 0 to the length of the string.

When you run this script, it will print `['a', 'ab', 'abc']`, which are all the prefixes of the string `'abc'`.