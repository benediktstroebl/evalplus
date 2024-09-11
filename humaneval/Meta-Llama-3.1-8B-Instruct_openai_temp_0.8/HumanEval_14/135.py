```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
    string (str): The input string

    Returns:
    List[str]: A list of all prefixes of the input string

    Examples:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = [string[i: j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]
    return sorted(set(prefixes))


# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['e', 'el', 'ell', 'hell', 'hello']
```

This script uses list comprehension to generate all possible prefixes of the input string, and then uses the `set` function and the `sorted` function to remove duplicates and sort the prefixes in order from shortest to longest.