```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.
    """
    # Initialize an empty list to store prefixes
    prefixes = []

    # Iterate over the string from the first character to the last
    for i in range(1, len(string) + 1):
        # Append the prefix of length i to the list
        prefixes.append(string[:i])

    # Return the list of prefixes
    return prefixes

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```