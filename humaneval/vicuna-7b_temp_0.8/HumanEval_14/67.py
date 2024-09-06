from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Build list of characters in string
    characters = string.lower()

    # Initialize list of prefixes
    prefixes = []

    # Iterate through characters
    for char in characters:
        # Create prefix
        prefix = ""
        for i in range(len(char)):
            prefix = prefix + char[i]

        # Add prefix to list
        prefixes.append(prefix)

    return prefixes

