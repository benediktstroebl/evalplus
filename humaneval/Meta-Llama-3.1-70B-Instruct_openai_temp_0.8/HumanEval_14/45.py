```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return a list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of prefixes from shortest to longest.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    # Initialize an empty list to store the prefixes
    prefixes = []

    # Iterate over the string, generating prefixes of increasing length
    for i in range(1, len(string) + 1):
        # Append the prefix to the list
        prefixes.append(string[:i])

    # Return the list of prefixes
    return prefixes

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']

# Alternatively, you can use a list comprehension to achieve the same result in a more concise way
def all_prefixes_concise(string: str) -> List[str]:
    """
    Return a list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of prefixes from shortest to longest.
    """
    return [string[:i] for i in range(1, len(string) + 1)]

# Test the concise function
print(all_prefixes_concise('abc'))  # Output: ['a', 'ab', 'abc']
```