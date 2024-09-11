```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
    string (str): The input string

    Returns:
    List[str]: A list of all prefixes of the input string

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

This script defines a function `all_prefixes` that takes a string as an input and returns a list of all its prefixes. The function uses a for loop to generate all prefixes by slicing the input string at each possible position, from the shortest to the longest. The test at the end demonstrates the function's usage. 

When you run this script, it will print `['a', 'ab', 'abc']`, which are all the prefixes of the string `'abc'`.