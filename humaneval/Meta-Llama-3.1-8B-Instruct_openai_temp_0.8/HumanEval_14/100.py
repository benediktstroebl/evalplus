```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    
    Args:
    string (str): The input string
    
    Returns:
    List[str]: A list of all prefixes of the input string in order from shortest to longest
    
    Example:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    
    # Initialize an empty list to store all prefixes
    prefixes = []
    
    # Iterate over the length of the string
    for i in range(1, len(string) + 1):
        # Append the prefix of the current length to the list
        prefixes.append(string[:i])
    
    # Return the list of all prefixes
    return prefixes

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all its prefixes, from shortest to longest. The function works by iterating over the length of the string, appending the prefix of the current length to the list, and finally returning the list of all prefixes.