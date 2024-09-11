```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string

    Returns:
        List[str]: A list of all prefixes of the input string
    """
    return [string[:i+1] for i in range(len(string))]


# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script uses list comprehension to generate all prefixes of the input string. The expression `string[:i+1]` generates the prefix of the string up to the `i+1`th character. The `range(len(string))` generates indices for all characters in the string.