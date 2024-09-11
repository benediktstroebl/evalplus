```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string

    Returns:
        List[str]: A list of prefixes from shortest to longest
    """
    # Initialize an empty list to store the prefixes
    prefixes = []
    
    # Iterate over the length of the input string
    for i in range(1, len(string) + 1):
        # Append the prefix of the current length to the list
        prefixes.append(string[:i])
    
    # Return the list of prefixes
    return prefixes

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```