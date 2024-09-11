```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    
    Args:
    string (str): The input string.
    
    Returns:
    List[str]: A list of all prefixes of the input string.
    
    Example:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []  # Initialize an empty list to store prefixes
    for i in range(len(string) + 1):  # Iterate over the string with index i
        prefix = string[:i]  # Get the substring from the start to index i
        prefixes.append(prefix)  # Add the prefix to the list
    return prefixes  # Return the list of prefixes


# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```