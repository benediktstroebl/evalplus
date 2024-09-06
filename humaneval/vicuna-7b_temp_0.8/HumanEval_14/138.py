from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Convert input string to lowercase and remove whitespace
    string = string.lower().strip()
    # Initialize prefixes list
    prefixes = []
    # Iterate over each character in the input string
    for c in string:
        # If current character is not whitespace and not a letter,
        # add prefixes from the previous character to the list
        if not c.isspace() and c.isalpha():
            prefixes.extend(prefixes[:-1] + [c])
        # If current character is a letter, append it to prefixes list
        else:
            prefixes.append(c)
    # Return list of prefixes
    return prefixes

