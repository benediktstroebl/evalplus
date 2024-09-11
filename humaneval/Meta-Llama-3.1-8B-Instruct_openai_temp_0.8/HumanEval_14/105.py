```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string, sorted from shortest to longest.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]


# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
print(all_prefixes('abcde'))  # Output: ['a', 'ab', 'abc', 'abcd', 'abcde']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the string, sorted from shortest to longest. The function uses a list comprehension to generate the prefixes by slicing the string from the start up to each index `i` (inclusive). The `range(len(string))` generates indices from 0 to the length of the string minus 1. The `+1` is used because string indexing in Python starts at 0. The function is then tested with three different strings to demonstrate its usage.