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
    # Initialize an empty list to store prefixes
    prefixes = []
    
    # Iterate over the length of the input string
    for length in range(1, len(string) + 1):
        # Extract the prefix of the current length
        prefix = string[:length]
        
        # Add the prefix to the list
        prefixes.append(prefix)
    
    # Return the list of prefixes
    return prefixes

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the string, from shortest to longest. The function uses a loop to iterate over the length of the input string, extracting each prefix of the current length and adding it to the list. The list of prefixes is then returned.