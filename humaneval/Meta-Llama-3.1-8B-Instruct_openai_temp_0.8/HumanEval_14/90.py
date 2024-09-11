```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    
    Args:
        string (str): The input string from which prefixes are generated.
    
    Returns:
        List[str]: A list of all prefixes of the input string, in order from shortest to longest.
    
    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    # Initialize an empty list to store all prefixes
    prefixes = []
    
    # Iterate over the length of the string, starting from 1 and going up to the length of the string
    for i in range(1, len(string) + 1):
        # Extract the substring of the input string from index 0 to i, and add it to the list of prefixes
        prefixes.append(string[:i])
    
    # Return the list of prefixes
    return prefixes

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all its prefixes, from shortest to longest. It achieves this by iterating over the length of the string, extracting substrings of increasing length, and adding them to the list of prefixes. The function is then tested with two example inputs: `'abc'` and `'hello'`.