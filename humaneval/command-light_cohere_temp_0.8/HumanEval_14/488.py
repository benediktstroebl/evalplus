Here is a self-contained Python function that solves the problem of finding all prefixes of a given string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Create an empty list to store the prefixes
    prefixes = []

    # Insert the shortest prefix first
    prefixes.append(string[0])

    # Iterate over the string length
    i = 1
    while i < len(string):
        # Insert the character before the current position
        prefixes.append(string[i])

        # Increment the index for the next character
        i += 1

    return prefixes
```
This function takes a string as input and returns a list of all its prefixes, from shortest to longest. It iterates over the advantage in Python and creates a list of all the prefixes. 

It uses the typing module to ensure that the function signature is correct and can be used with other typing-related features.