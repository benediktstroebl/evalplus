```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    Parameters:
    string (str): The input string
    Returns:
    List[str]: A list of all prefixes of the input string
    """
    # Initialize an empty list to store the prefixes
    prefixes = []
    
    # Iterate over the string with a variable 'i' that ranges from 1 to the length of the string
    for i in range(1, len(string) + 1):
        # For each 'i', extract the prefix and append it to the list
        prefixes.append(string[:i])
    
    # Return the list of prefixes
    return prefixes


# Test the function
print(all_prefixes('abc'))  # Expected output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the string, from shortest to longest. The script then tests this function with the input string `'abc'`.