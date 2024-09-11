```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Initialize an empty list to store the prefixes
    prefixes = []
    
    # Iterate over the string, slicing from the start to the current index + 1
    for i in range(1, len(string) + 1):
        # Append the prefix to the list
        prefixes.append(string[:i])
    
    # Return the list of prefixes
    return prefixes

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the string. The function uses a for loop to iterate over the string, slicing from the start to the current index + 1 to generate each prefix. The prefixes are then appended to a list, which is returned at the end of the function. The example usage demonstrates how to use the function with the input string 'abc'.