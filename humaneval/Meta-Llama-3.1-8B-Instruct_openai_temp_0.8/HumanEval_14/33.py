```markdown
### Function to Generate All Prefixes of a String

This script defines a function `all_prefixes` that generates all prefixes of a given string, sorted by length from shortest to longest.

```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string, sorted by length.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    # Initialize an empty list to store all prefixes
    prefixes = []

    # Iterate over the length of the string
    for length in range(1, len(string) + 1):
        # Slice the string to get the prefix of the current length
        prefix = string[:length]
        # Append the prefix to the list
        prefixes.append(prefix)

    # Sort the list of prefixes by length
    prefixes.sort()

    # Return the sorted list of prefixes
    return prefixes

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script first iterates over the length of the input string, slicing the string to get each prefix. It then sorts the list of prefixes by length before returning it. The result is a list of all prefixes of the input string, sorted by length from shortest to longest.