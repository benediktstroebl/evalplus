```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Example usage
print(all_prefixes('abc'))
```

In this code, we use a list comprehension to generate all prefixes of the input string. The expression `string[:i+1]` gets the substring from the start of the string to the `i-th` character (inclusive). We use `range(len(string))` to generate numbers from 0 to `len(string) - 1`, which correspond to the length of each prefix.

When you run this script, it will print `['a', 'ab', 'abc']`, which are all the prefixes of `'abc'`.