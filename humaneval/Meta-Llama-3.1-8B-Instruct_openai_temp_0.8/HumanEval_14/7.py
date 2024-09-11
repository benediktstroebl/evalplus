```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string

    Returns:
        List[str]: A list of all prefixes in the input string, in order from shortest to longest
    """
    # Initialize an empty list to store all prefixes
    prefixes = []
    
    # Iterate over the length of the string, starting from 1 and going up to the length of the string
    for length in range(1, len(string) + 1):
        # Extract the prefix of the current length from the string
        prefix = string[:length]
        
        # Add the prefix to the list of prefixes
        prefixes.append(prefix)
    
    # Return the list of prefixes
    return prefixes

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the string, in order from shortest to longest. It uses a loop to iterate over the length of the string, extracting each prefix in turn and adding it to the list. The function includes a docstring that explains its purpose, arguments, and return value. The script also includes a test call to the function to demonstrate its usage.