```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string

    Returns:
        List[str]: A list of prefixes

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    # Initialize an empty list to store prefixes
    prefixes = []

    # Iterate over the length of the string from 1 to the length of the string
    for length in range(1, len(string) + 1):
        # Slice the string from the start to the current length to get the prefix
        prefix = string[:length]
        # Append the prefix to the list
        prefixes.append(prefix)

    # Return the list of prefixes
    return prefixes

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```