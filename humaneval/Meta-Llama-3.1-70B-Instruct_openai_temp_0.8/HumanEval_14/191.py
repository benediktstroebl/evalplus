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
    return [string[:i+1] for i in range(len(string))]

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that uses a list comprehension to generate all prefixes of the input string. The list comprehension iterates over the indices of the string, slicing the string up to each index `i+1` to generate the prefix. The result is a list of all prefixes from shortest to longest.

To run the script, save it to a file (e.g., `prefixes.py`), then run it using Python (e.g., `python prefixes.py`). The example usage at the end of the script will print the list of prefixes for the string `'abc'`.