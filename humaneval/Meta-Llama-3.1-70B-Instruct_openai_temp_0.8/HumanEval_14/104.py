```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return a list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.

    Examples:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]


# Example usage:
if __name__ == "__main__":
    print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines the `all_prefixes` function as specified. It uses a list comprehension to generate all prefixes of the input string. The `string[:i]` expression generates a prefix of length `i`, and the `range(1, len(string) + 1)` ensures that prefixes of all lengths from 1 to the full length of the string are generated.

The script also includes an example usage of the `all_prefixes` function in the `if __name__ == "__main__":` block, which is a common pattern in Python scripts to ensure that example usage is only executed when the script is run directly, not when it is imported as a module by another script.