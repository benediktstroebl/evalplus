```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string from which to generate prefixes.

    Returns:
        List[str]: A list of all prefixes of the input string, sorted from shortest to longest.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    # Initialize an empty list to store prefixes
    prefixes = []
    
    # Iterate over the length of the string
    for length in range(1, len(string) + 1):
        # Generate a prefix of the current length
        prefix = string[:length]
        # Add the prefix to the list
        prefixes.append(prefix)
    
    # Return the list of prefixes
    return prefixes

# Example usage
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

In this script, we use a loop to generate all prefixes of the input string by slicing the string from the start to the current length. The list of all prefixes is then returned.