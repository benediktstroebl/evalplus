```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string

    Returns:
        List[str]: A list of all prefixes from shortest to longest

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

In this script, we use a simple loop to generate all prefixes of the input string. The `string[:i]` expression slices the string to get the first `i` characters. We start from `i=1` because an empty string is considered a prefix of any string. The `range(1, len(string) + 1)` function generates numbers from 1 to the length of the string. The prefixes are then returned as a list.

When you run this script, it will print `['a', 'ab', 'abc']`, which are all the prefixes of the string `'abc'` from shortest to longest.