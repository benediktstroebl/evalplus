```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string

    Returns:
        List[str]: A list of all prefixes in the string

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        # Get all substrings of the input string of length i
        prefixes.extend([string[j:i] for j in range(len(string) - i + 1)])
    # Remove duplicates by converting list to set and back to list
    return list(set(prefixes))

# Test the function
print(all_prefixes('abc'))
print(all_prefixes('hello'))
```