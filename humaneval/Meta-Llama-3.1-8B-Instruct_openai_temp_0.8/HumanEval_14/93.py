### Prefix Generation Script
```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
    string (str): The input string from which prefixes will be generated.

    Returns:
    List[str]: A list of prefixes, ordered from shortest to longest.

    Example:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Initialize an empty list to store the prefixes
    prefixes = []
    
    # Iterate over the string, generating prefixes of all lengths
    for length in range(1, len(string) + 1):
        # Slice the string to get the prefix of the current length
        prefix = string[:length]
        # Add the prefix to the list
        prefixes.append(prefix)
    
    # Return the list of prefixes
    return prefixes

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```
This script defines a function `all_prefixes` that generates all prefixes of a given string, from shortest to longest. The example usage shows how to call the function with different input strings and print the resulting lists of prefixes.