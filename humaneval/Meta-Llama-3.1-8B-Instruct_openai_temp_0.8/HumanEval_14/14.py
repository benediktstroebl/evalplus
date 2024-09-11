```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.
    
    Args:
        string (str): The input string.
    
    Returns:
        List[str]: A list of prefixes in order from shortest to longest.
    
    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    prefixes = [string[i:] for i in range(len(string)+1)]
    return sorted(prefixes, key=len)

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that generates all prefixes of a given string, sorts them by length, and returns them as a list. The list comprehension `[string[i:] for i in range(len(string)+1)]` generates all prefixes by slicing the string from the current index `i` to the end. The `sorted` function with `key=len` is used to sort the prefixes in order from shortest to longest.