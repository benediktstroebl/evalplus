```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    Args:
        string (str): Input string
    Returns:
        List[str]: A list of prefixes in order of length from shortest to longest
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []  # Initialize an empty list to store prefixes
    for length in range(1, len(string) + 1):  # Iterate over possible prefix lengths
        prefix = string[:length]  # Extract the prefix of the current length
        prefixes.append(prefix)  # Add the prefix to the list
    return prefixes  # Return the list of prefixes

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines the `all_prefixes` function which takes a string as input and returns a list of all prefixes of the string, from shortest to longest. It achieves this by iterating over possible prefix lengths, extracting the corresponding prefix from the input string, and adding it to the list of prefixes. Finally, it returns the list of prefixes.