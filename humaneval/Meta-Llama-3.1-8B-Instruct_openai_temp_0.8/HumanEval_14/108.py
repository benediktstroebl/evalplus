```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
    string (str): Input string.

    Returns:
    List[str]: List of prefixes.

    Example:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefix = string[:i]
        prefixes.append(prefix)
    return sorted(prefixes)


# Test the function
if __name__ == "__main__":
    print(all_prefixes('abc'))
    # Output: ['a', 'ab', 'abc']
```

This script uses a loop to generate all possible prefixes of the input string, and then sorts them in ascending order. The `sorted()` function is used with no arguments, which means it sorts the list in ascending order by default.