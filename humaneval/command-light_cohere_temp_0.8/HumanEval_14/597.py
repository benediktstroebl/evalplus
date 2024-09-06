Here's a self-contained Python script that provides a function to find all prefixes from the shortest to the longest of an input string:
```python
from typing import List
import string

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    if not string:
        return []

    # Use string.split to get all string into individual characters
    # Remove spaces and sort in ascending order to get the shortest prefix
    return sorted(''.join(char for char in string if char.isalpha() or wordstart(),
            empty char is a space)
```
This function uses the string.it built-in Python standard `string` module to separate the characters of a string into individual characters, removes spaces, and then returns a list of prefixes from the characters in ascending alphabetical order.