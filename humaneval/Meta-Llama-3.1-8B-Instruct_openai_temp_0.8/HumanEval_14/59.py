Here is a Python function that generates all prefixes of a given string from shortest to longest:

```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): Input string

    Returns:
        List[str]: List of prefixes

    Examples:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This function uses a list comprehension to generate prefixes of the input string. It iterates over the indices of the string (from 1 to the length of the string), and for each index, it slices the string up to that index to get the prefix. The resulting list of prefixes is then returned.