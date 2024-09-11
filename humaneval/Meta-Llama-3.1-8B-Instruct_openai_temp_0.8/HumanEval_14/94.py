```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): Input string.

    Returns:
        List[str]: List of prefixes.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i + 1] for i in range(len(string))]

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes from shortest to longest. The function uses a list comprehension to generate the prefixes. The `[:i + 1]` slice operation is used to get the substring from the start of the string up to the current index `i`. The `range(len(string))` function generates the indices from 0 to the length of the string, which are used to iterate over the string.