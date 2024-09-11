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
    return [string[:i+1] for i in range(len(string))]

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script uses a list comprehension to generate all prefixes of the input string. The outer list comprehension iterates over the range of indices in the string, and for each index `i`, it creates a string slice `string[:i+1]`, which is the prefix of the string up to and including the character at index `i`. The `+1` is needed because the slice operator in Python is exclusive of the end index. The result is a list of all prefixes of the input string, from shortest to longest.