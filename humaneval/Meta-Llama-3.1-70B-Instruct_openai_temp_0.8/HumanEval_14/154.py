```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Returns a list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of prefixes.

    Examples:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    # Initialize an empty list to store the prefixes
    prefixes = []
    
    # Iterate over the string from the first character to the last
    for i in range(1, len(string) + 1):
        # Append the prefix of the current length to the list
        prefixes.append(string[:i])
    
    # Return the list of prefixes
    return prefixes

# Example usage
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that takes an input string and returns a list of its prefixes. The function iterates over the string and appends each prefix to the list. The list is then returned. The example usage demonstrates how to use the function with the string `'abc'`.