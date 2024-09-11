```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
    string (str): The input string.

    Returns:
    List[str]: A list of all prefixes in the input string, from shortest to longest.

    Example:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the input string, from shortest to longest. The function uses a list comprehension to generate the prefixes by slicing the input string up to each possible index. The `range(len(string))` generates indices from 0 to the length of the string, and `string[:i+1]` slices the string up to each index `i`. The `+1` is needed because string indices in Python are 0-based, but we want to include the character at the current index in the prefix.