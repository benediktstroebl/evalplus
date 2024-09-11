```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of prefixes from the input string.
    """
    return [string[:i+1] for i in range(len(string))]


# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that uses list comprehension to generate a list of prefixes from the input string. It works by iterating over the indices of the string and slicing the string from the beginning to each index plus one, effectively generating all possible prefixes. The test at the end of the script demonstrates the function's usage.