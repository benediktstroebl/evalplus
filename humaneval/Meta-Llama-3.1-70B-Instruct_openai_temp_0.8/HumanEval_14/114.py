```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): Input string for which prefixes need to be generated.

    Returns:
        List[str]: List of all prefixes from shortest to longest of the input string.
    """
    # Initialize an empty list to store the prefixes.
    prefixes = []
    
    # Iterate over the string from the first character to the last.
    for i in range(1, len(string) + 1):
        # Append the prefix of the current length to the list.
        prefixes.append(string[:i])
    
    # Return the list of prefixes.
    return prefixes


# Test the function with the provided example.
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```