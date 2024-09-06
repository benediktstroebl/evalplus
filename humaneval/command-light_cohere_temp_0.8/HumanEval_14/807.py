Here is a self-contained Python function that solves the problem of finding all prefixes from shortest to longest of an input string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    if not string:
        return []

    # Create an empty list to store the prefixes
    prefixes = []

    # Loop until the start of the next prefix is found
    for i in range(1, len(string) + 1):
        # If the current character is the start of a new prefix, add it to the list
        if string[i - 1] != string[i]:
            prefixes.append(string[i -
            )

    return prefixes
```

This function uses a loop to iterate over each character in the string, appending only the characters that are not the start of a new prefix.

It uses the `typing` module to add type annotations. This helps to improve the readability and maintainability of the code. 

This code is self-contained and does not require any external functions or modules.