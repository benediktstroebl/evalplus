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

This script defines a function `all_prefixes` that generates all prefixes of a given string. It achieves this by iterating over the string with a loop, and at each step, it appends a substring of the original string to the list of prefixes. The length of the substring is determined by the current iteration number `i`. 

The script then tests the function with the example provided in the documentation string. When you run this script, it will print `['a', 'ab', 'abc']`, which are all the prefixes of `'abc'` in order of length from shortest to longest.