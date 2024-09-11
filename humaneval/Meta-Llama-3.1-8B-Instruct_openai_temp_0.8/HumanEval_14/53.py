```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
    string (str): The input string from which prefixes will be generated

    Returns:
    List[str]: A list of all prefixes of the input string, sorted by length

    Example:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Initialize an empty list to store all prefixes
    prefixes = []
    
    # Iterate over the string with a sliding window of increasing size
    for i in range(1, len(string) + 1):
        # Extract the prefix of the current size
        prefix = string[:i]
        # Append the prefix to the list
        prefixes.append(prefix)
    
    # Return the list of prefixes
    return prefixes


# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines the `all_prefixes` function, which generates all prefixes of the input string and returns them in a sorted list. The function iterates over the string with a sliding window of increasing size, extracting each prefix and appending it to the list. The script also includes example usage and test cases to demonstrate the function's behavior.