```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    # Use list comprehension to generate all prefixes
    # The outer loop iterates over the string
    # The inner loop generates prefixes of increasing length
    return [string[:i] for i in range(1, len(string) + 1)]

# Test the function
print(all_prefixes('abc'))  # ['a', 'ab', 'abc']
print(all_prefixes(''))      # ['']
print(all_prefixes('a'))     # ['a']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the string, from shortest to longest. The function uses list comprehension to generate the prefixes. The outer loop iterates over the string, and the inner loop generates prefixes of increasing length. The script includes example use cases to demonstrate the function's behavior.