```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']

    :param string: Input string
    :return: List of all prefixes from shortest to longest
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        # Append slice of string from start to current index to get prefix
        prefixes.append(string[:i])
    return prefixes

# Example usage
print(all_prefixes('abc'))
```
This script defines a function `all_prefixes` that generates all prefixes of a given string by iterating over the string's length. It uses Python's string slicing feature (`string[:i]`) to get the prefix up to the current index `i`. The function then returns the list of prefixes in order from shortest to longest. The example usage at the end demonstrates how to use this function to get all prefixes of the string `'abc'`.