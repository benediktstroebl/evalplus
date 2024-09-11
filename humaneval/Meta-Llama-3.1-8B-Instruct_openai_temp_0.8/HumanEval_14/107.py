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
    prefixes = [string[:i+1] for i in range(len(string))]
    return prefixes

# Test the function
print(all_prefixes('abc'))
```

This script defines a function `all_prefixes` that generates all prefixes of a given string. It uses a list comprehension to generate the prefixes by slicing the input string for each possible length. The function is then tested with the example input 'abc'.