```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.
    """
    return [string[:i+1] for i in range(len(string))]

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that uses list comprehension to generate all prefixes of the input string. It does this by iterating over the characters in the string and slicing the string from the start to each character index, incrementing by 1 each time. The result is a list of all prefixes of the input string, from shortest to longest.