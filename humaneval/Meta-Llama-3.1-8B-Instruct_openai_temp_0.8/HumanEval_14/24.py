```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
    string (str): The input string for which all prefixes are to be found

    Returns:
    List[str]: A list of all prefixes in the input string, from shortest to longest

    Example:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Test the function
print(all_prefixes('abc'))
```

This script defines a function `all_prefixes` that uses a list comprehension to generate all prefixes of the input string. The `range(len(string))` is used to iterate over the length of the string, and `string[:i+1]` is used to get the prefix of length `i+1`. The result is a list of all prefixes, from shortest to longest.