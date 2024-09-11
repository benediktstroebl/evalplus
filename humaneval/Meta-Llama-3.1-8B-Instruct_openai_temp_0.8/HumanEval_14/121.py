```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of prefixes in order from shortest to longest.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    # Initialize an empty list to store the prefixes
    prefixes = []

    # Iterate over the string with an index and a character
    for i in range(len(string)):
        # Extract the prefix of length i+1
        prefix = string[:i+1]
        
        # Add the prefix to the list
        prefixes.append(prefix)

    # Return the list of prefixes
    return prefixes

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all its prefixes from shortest to longest. It does this by iterating over the string and extracting prefixes of increasing length. The function is then tested with two example strings.