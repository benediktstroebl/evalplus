```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    
    Parameters:
    string (str): Input string
    
    Returns:
    List[str]: List of all prefixes
    
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

This script defines a function `all_prefixes` that takes a string as input and returns a list of all its prefixes, from shortest to longest. The function uses a loop to iterate over the length of the string, slicing the string at each position to get the prefix. The prefixes are then returned in a list. The test at the end demonstrates the function's behavior with the input string 'abc'.