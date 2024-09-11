### Prefixes of a String
Here's a Python function that generates all prefixes of a given string from shortest to longest.

```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string for which prefixes are generated.

    Returns:
        List[str]: A list of all prefixes of the input string, from shortest to longest.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script uses a list comprehension to generate prefixes of the input string. It iterates over the length of the string, slicing the string from the start to the current index `i+1` (since string slicing in Python is exclusive of the end index). The resulting prefixes are collected in a list, which is then returned.