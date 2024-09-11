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
    # Initialize an empty list to store the prefixes
    prefixes = []

    # Loop through the string with two nested loops to generate all prefixes
    for i in range(1, len(string) + 1):
        # Use string slicing to get the prefix of the current length
        prefix = string[:i]
        # Add the prefix to the list
        prefixes.append(prefix)

    # Return the list of prefixes
    return prefixes

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script uses a simple nested loop approach to generate all prefixes of the input string. It slices the string to get the prefix of the current length at each iteration, and adds it to the list of prefixes. Finally, it returns the list of prefixes. The example usage demonstrates how to use the `all_prefixes` function with different input strings.