```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): Input string.

    Returns:
        List[str]: List of all prefixes.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    # Initialize an empty list to store the prefixes
    prefixes = []
    
    # Iterate over the length of the string
    for length in range(1, len(string) + 1):
        # Slice the string to get the prefix of the current length
        prefix = string[:length]
        # Append the prefix to the list
        prefixes.append(prefix)
    
    # Return the list of prefixes
    return prefixes

# Test the function
print(all_prefixes('abc'))  # ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # ['h', 'he', 'hel', 'hell', 'hello']
```