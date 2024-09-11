```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string for which all prefixes are generated

    Returns:
        List[str]: A list of all prefixes of the input string in order from shortest to longest

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    # Initialize an empty list to store the prefixes
    prefixes = []

    # Iterate over the string with the index and character
    for i in range(len(string)):
        # Extract the prefix from the string up to the current index
        prefix = string[:i+1]
        # Append the prefix to the list
        prefixes.append(prefix)

    # Return the list of prefixes
    return prefixes


# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the string, from shortest to longest. The function uses a loop to iterate over the string, extracting each prefix as it goes and appending it to a list. Finally, the function returns the list of prefixes. The script also includes a test of the function with two example inputs.