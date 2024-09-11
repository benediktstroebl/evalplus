```markdown
### All Prefixes of a String

This Python script generates a list of all prefixes of a given string, 
sorted from shortest to longest.

```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of prefixes.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    # Initialize an empty list to store prefixes
    prefixes = []

    # Loop through the string with a sliding window of increasing size
    for i in range(1, len(string) + 1):
        # Append the current prefix to the list
        prefixes.append(string[:i])

    # Return the list of prefixes
    return prefixes

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```