```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.

    Examples:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]


# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that takes an input string and returns a list of all its prefixes, from shortest to longest. The function uses a list comprehension to generate the prefixes. The `[:i+1]` slice is used to get the substring from the start of the string up to the `i+1`th character. The `range(len(string))` generates indices from 0 to the length of the string minus 1.

You can save this script to a file, for example `all_prefixes.py`, and run it with Python to test the function.