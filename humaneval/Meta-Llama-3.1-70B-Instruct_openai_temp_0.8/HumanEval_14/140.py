```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string

    Returns:
        List[str]: List of all prefixes from shortest to longest
    """
    return [string[:i+1] for i in range(len(string))]


# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```