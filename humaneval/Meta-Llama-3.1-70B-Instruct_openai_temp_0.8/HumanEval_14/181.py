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
    # Initialize an empty list to store the prefixes.
    prefixes = []
    
    # Iterate over the range from 1 to the length of the string (inclusive).
    # This is because we want to generate all prefixes from length 1 to the full string.
    for i in range(1, len(string) + 1):
        # Append the substring from the start of the string to the current index to the list of prefixes.
        prefixes.append(string[:i])
    
    # Return the list of prefixes.
    return prefixes


# Test the function.
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']

# Test the function with an empty string.
print(all_prefixes(''))  # Output: []

# Test the function with a single character string.
print(all_prefixes('a'))  # Output: ['a']
```