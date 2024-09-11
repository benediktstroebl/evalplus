```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    Parameters:
    string (str): Input string

    Returns:
    List[str]: List of prefixes

    Example:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Use list comprehension to generate all prefixes
    # range(len(string) + 1) generates indices from 0 to len(string)
    # string[:i] generates prefixes of string at each index i
    return [string[:i] for i in range(1, len(string) + 1)]


# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```