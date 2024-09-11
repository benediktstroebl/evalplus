```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    Args:
        string (str): The input string
    
    Returns:
        List[str]: A list of all prefixes of the input string
    """
    # Initialize an empty list to store the prefixes
    prefixes = []
    
    # Iterate over the length of the string
    for length in range(1, len(string) + 1):
        # Get the prefix of the current length
        prefix = string[:length]
        # Append the prefix to the list
        prefixes.append(prefix)
    
    return prefixes


# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This code defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the string. It does this by iterating over the lengths of the string (from 1 to the length of the string) and appending the prefix of the current length to the list. The function is then tested with the example 'abc'.