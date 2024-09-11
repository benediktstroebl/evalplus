```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): Input string.

    Returns:
        List[str]: List of all prefixes.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    # Initialize an empty list to store prefixes
    prefixes = []
    
    # Loop through the length of the string
    for i in range(1, len(string) + 1):
        # Get the prefix by slicing the string up to the current length
        prefix = string[:i]
        
        # Append the prefix to the list
        prefixes.append(prefix)
    
    # Return the list of prefixes
    return prefixes

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```