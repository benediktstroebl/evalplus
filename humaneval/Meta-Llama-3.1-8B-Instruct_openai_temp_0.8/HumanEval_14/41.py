```python
from typing import List
import itertools


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string, from shortest to longest.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    # Generate all possible suffixes of the string by iterating over the string's possible suffix lengths
    suffixes = [''.join(p) for p in itertools.product(string, repeat=range(1, len(string) + 1))]
    
    # Return the prefixes, which are the strings that are not included in the suffixes
    return [s for s in string for substring in suffixes if s in substring]


# Test the function
print(all_prefixes('abc'))
```

However, the given task seems a bit misleading as it asks for all prefixes (suffixes) of a string. If we are looking for all prefixes of a string, we should actually generate all substrings from the start of the string to the end. Here's a revised version of the function:

```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string, from shortest to longest.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    # Generate all prefixes by slicing the string
    prefixes = [string[:i+1] for i in range(len(string))]
    
    # Return the prefixes
    return prefixes


# Test the function
print(all_prefixes('abc'))
```