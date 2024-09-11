```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): Input string

    Returns:
        List[str]: List of all prefixes

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes

# Test the function
print(all_prefixes('abc'))
```

In this script, we define a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the string. We iterate over the range from 1 to the length of the string (inclusive), and for each index `i`, we append the substring of the input string up to index `i` to the list of prefixes. Finally, we return the list of prefixes.