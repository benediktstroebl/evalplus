```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of prefixes from shortest to longest.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script uses list comprehension to generate all prefixes of the input string. It iterates over each character in the string (using `range(len(string))`) and slices the string from the start up to the current character index plus one (`string[:i+1]`). The result is a list of all prefixes from shortest to longest.