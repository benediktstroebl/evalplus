```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Initialize an empty list to store prefixes
    prefixes = []
    
    # Iterate over the length of the string
    for length in range(1, len(string) + 1):
        # Slice the string to get the prefix of the current length
        prefix = string[:length]
        # Add the prefix to the list
        prefixes.append(prefix)
    
    # Return the list of prefixes
    return prefixes

# Test the function
print(all_prefixes('abc'))
```

This script uses a for loop to iterate over the length of the string, and for each length, it slices the string to get the prefix of that length. It then adds that prefix to the list of prefixes. The function finally returns the list of prefixes.

When you run this script, it will print: `['a', 'ab', 'abc']`, which are all the prefixes of the string `'abc'` from shortest to longest.