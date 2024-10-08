```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
    string (str): Input string

    Returns:
    List[str]: List of all prefixes of the input string

    Example:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    # Initialize an empty list to store the prefixes
    prefixes = []

    # Generate all prefixes
    for length in range(1, len(string) + 1):
        # Get the substring from the start to the current length
        prefix = string[:length]
        # Append the prefix to the list
        prefixes.append(prefix)

    # Return the list of prefixes
    return prefixes


# Test the function
print(all_prefixes('abc'))
```

This script defines a function `all_prefixes` that generates all prefixes of the input string and returns them as a list. The prefixes are generated by iterating over the string and getting substrings of increasing lengths. The function is tested with the example 'abc'.