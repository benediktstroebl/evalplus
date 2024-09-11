```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.
    
    Args:
        string (str): The input string.
    
    Returns:
        List[str]: A list of all prefixes of the input string.
    """
    # Initialize an empty list to store the prefixes
    prefixes = []
    
    # Iterate over the string with its index
    for i in range(len(string)):
        # For each index, append the substring up to that index to the list
        prefixes.append(string[:i+1])
    
    # Return the list of prefixes
    return prefixes

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script uses a simple loop to generate all prefixes of the input string by slicing the string up to each index. The resulting prefixes are stored in a list and returned at the end. The example usage at the end demonstrates how to use the function.