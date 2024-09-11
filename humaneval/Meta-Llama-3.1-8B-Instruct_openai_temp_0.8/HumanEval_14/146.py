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
        # Slice the string up to the current length and add it to the list
        prefixes.append(string[:i])
    
    return prefixes

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script works by iterating over the length of the input string, and for each length, it slices the string up to that length and adds it to the list of prefixes. The function returns this list of prefixes.