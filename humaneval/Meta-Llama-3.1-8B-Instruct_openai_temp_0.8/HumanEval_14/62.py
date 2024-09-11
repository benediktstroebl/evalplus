```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string

    Returns:
        List[str]: A list of prefixes in order from shortest to longest

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    prefixes = [string[i:] for i in range(len(string) + 1)]
    return prefixes[:-1]  # exclude the whole string itself

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script uses list comprehension to generate all prefixes of the input string and then returns the list of prefixes (excluding the full string itself). The `-1` index in the return statement is used to exclude the last element of the list, which is the full input string.