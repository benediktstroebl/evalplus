```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return a list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes from shortest to longest.

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Initialize an empty list to store the prefixes
    prefixes = []

    # Iterate over the length of the string (from 1 to n)
    for length in range(1, len(string) + 1):
        # Extract the prefix of the current length and add it to the list
        prefixes.append(string[:length])

    # Return the list of prefixes
    return prefixes

# Test the function
print(all_prefixes('abc'))
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes from shortest to longest. It uses a loop to iterate over the length of the string and extract the prefix of each length. The list of prefixes is then returned. The script includes a docstring that explains the purpose and behavior of the function, as well as a test case to demonstrate its usage.