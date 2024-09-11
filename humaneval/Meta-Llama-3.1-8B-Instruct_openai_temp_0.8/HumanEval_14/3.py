### All Prefixes of a String
#### Problem Statement

Return a list of all prefixes from shortest to longest of the input string.

#### Solution

```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes from shortest to longest.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    # Initialize an empty list to store the prefixes
    prefixes = []

    # Iterate over the length of the string
    for i in range(1, len(string) + 1):
        # Extract the prefix of the current length
        prefix = string[:i]
        # Append the prefix to the list
        prefixes.append(prefix)

    # Return the list of prefixes
    return prefixes

# Example usage
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes from shortest to longest. The function uses a loop to iterate over the length of the string, extracting the prefix of each length and appending it to the list. The function then returns the list of prefixes. The example usage demonstrates how to call the function with different input strings.