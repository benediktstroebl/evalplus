```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes.

    Examples:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]


# Example usage:
if __name__ == "__main__":
    print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that uses a list comprehension to generate all prefixes of the input string by iterating over the string's length and slicing the string up to each index. The result is a list of all prefixes from the shortest to the longest.