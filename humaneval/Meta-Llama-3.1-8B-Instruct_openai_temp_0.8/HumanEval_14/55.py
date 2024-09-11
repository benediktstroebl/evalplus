### Generating All Prefixes of a String

Below is a Python script that uses a list comprehension to generate all prefixes of a given string, from the shortest to the longest.

```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Test the function
print(all_prefixes('abc'))
```

In this script, we use a list comprehension to generate all prefixes of the input string. The expression `string[:i+1]` generates a prefix of the string from the beginning up to the `i-th` character (excluding the `i-th` character). The outer `[...]` just puts all these prefixes together into a list. The `range(len(string))` generates indices from 0 up to the last index of the string.