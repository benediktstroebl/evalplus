```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Returns a list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes.
    """
    return [string[:i + 1] for i in range(len(string))]

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```