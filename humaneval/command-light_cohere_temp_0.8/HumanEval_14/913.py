Here is a Python script that defines a function all_prefixes that finds all prefixes from shortest to longest of a given string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Remove all characters except a single character
    char = string[-1]
    string = ''.join(char, c for c in string if c != char)
    # Separate into prefix and suffix
    prefix = string[:-len(char)]
    suffix = string[-len(char):]
    # Return list of all prefixes
    return [prefix, suffix] + all_prefixes(suffix)
```