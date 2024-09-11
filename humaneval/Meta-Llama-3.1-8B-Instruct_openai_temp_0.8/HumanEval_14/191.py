```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.
    
    Args:
        string (str): The input string.
    
    Returns:
        List[str]: A list of all prefixes of the input string in order from shortest to longest.
    
    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    # Initialize an empty list to store the prefixes
    prefixes = []
    
    # Loop over all possible lengths of prefixes (from 1 to the length of the string)
    for length in range(1, len(string) + 1):
        # Extract the prefix of the current length
        prefix = string[:length]
        
        # Add the prefix to the list of prefixes
        prefixes.append(prefix)
    
    # Return the list of prefixes
    return prefixes

# Test the function
print(all_prefixes('abc'))
```