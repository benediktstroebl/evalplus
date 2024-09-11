```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string from which to generate prefixes.

    Returns:
        List[str]: A list of all prefixes of the input string, sorted from shortest to longest.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    # Initialize an empty list to store the prefixes
    prefixes = []

    # Generate all prefixes by slicing the string up to each position
    for i in range(len(string)):
        # Append the prefix to the list
        prefixes.append(string[:i+1])

    # Return the list of prefixes
    return prefixes

# Test the function
print(all_prefixes('abc'))
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all its prefixes, sorted from shortest to longest. The function uses a loop to generate each prefix by slicing the string up to each position, and stores the prefixes in a list. The list is then returned by the function. The script also includes a test case to demonstrate the function's behavior.