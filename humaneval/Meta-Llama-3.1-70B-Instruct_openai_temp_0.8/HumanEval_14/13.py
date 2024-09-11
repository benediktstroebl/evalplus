```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.
    """
    # Use a list comprehension to generate all prefixes
    # The range function generates numbers from 1 to the length of the string (inclusive)
    # For each number i, string[:i] generates the prefix of length i
    return [string[:i] for i in range(1, len(string) + 1)]


# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']


# Test the function
import doctest
doctest.testmod()
```