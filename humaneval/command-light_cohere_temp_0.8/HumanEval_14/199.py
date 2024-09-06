Here's a self-contained Python script that defines a function all_prefixes that returns a list of all prefixes from shortest to longest of a given input string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Returns list of all prefixes from shortest to longest of the input string.
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Use string.split() to split the first character of the string into a list of characters
    characters = string.split()

    # Initialize a result list to store the prefixes
    prefixes = []
    # Loop through the list of characters
    for char in characters:
        # If the character is the last one, add it to the result list
        if char == string[-1]:
            prefixes.append(char)
        # Otherwise append the last character as-by itself to the list of prefixes
        prefixes.append(char)
    return prefixes
```

This function uses the Split method to split the input string into a list of characters and then loops through the list of characters to add the character as a prefix and the character itself as a suffix. The function then returns a list of all prefixes.