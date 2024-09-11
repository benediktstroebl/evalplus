```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Returns a list of all prefixes from shortest to longest of the input string.

    Args:
    string (str): The input string.

    Returns:
    List[str]: A list of prefixes.

    Example:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]


# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

In this script, we define the `all_prefixes` function as specified. The function uses a list comprehension to generate all prefixes of the input string. It does this by slicing the string from the beginning up to each index `i` in the range from 1 to the length of the string (inclusive). The `range(1, len(string) + 1)` is used instead of `range(len(string))` to include the full string as the last prefix.

We then test the function with the example provided.