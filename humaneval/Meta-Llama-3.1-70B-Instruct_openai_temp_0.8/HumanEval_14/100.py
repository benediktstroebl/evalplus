```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return a list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes from shortest to longest.

    Examples:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]


# Example usage:
if __name__ == "__main__":
    print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script uses list comprehension to generate all prefixes of the input string. The `string[:i]` expression slices the string up to the `i-th` character, and the `range(1, len(string) + 1)` generates indices from 1 to the length of the string (inclusive). The result is a list of all prefixes from shortest to longest.