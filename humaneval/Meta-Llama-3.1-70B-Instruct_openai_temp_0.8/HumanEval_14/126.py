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
    
    # Iterate over the length of the string
    for length in range(1, len(string) + 1):
        # Append the substring from the start to the current length
        prefixes.append(string[:length])
    
    # Return the list of prefixes
    return prefixes

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```