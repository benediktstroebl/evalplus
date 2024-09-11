```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): Input string

    Returns:
        List[str]: List of prefixes

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    # Initialize an empty list to store prefixes
    prefixes = []
    
    # Iterate over the length of the input string
    for i in range(1, len(string) + 1):
        # Extract prefix of current length and add it to the list
        prefixes.append(string[:i])
    
    # Return the list of prefixes
    return prefixes

# Test the function
print(all_prefixes('abc'))
```

This script uses a simple for loop to generate all prefixes of the input string by slicing the string with varying start and end indices. The prefixes are then appended to a list, which is returned at the end of the function. The script also includes an example usage and docstring to explain the function's behavior.