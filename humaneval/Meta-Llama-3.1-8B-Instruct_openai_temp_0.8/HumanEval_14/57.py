```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string

    Returns:
        List[str]: A list of all prefixes of the input string

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]

# Test the function
if __name__ == "__main__":
    print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

In this script, we use a list comprehension to generate all prefixes of the input string. The `range(1, len(string) + 1)` function generates numbers from 1 to the length of the string, and `string[:i]` gets the prefix of the string up to the `i-th` character. The resulting list of prefixes is then returned.