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
    # Use a list comprehension to generate all prefixes of the input string
    # The range from 1 to len(string) + 1 is used to generate all possible prefix lengths
    # The string slicing operation string[:i] is used to get the prefix of length i
    return [string[:i] for i in range(1, len(string) + 1)]


# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```