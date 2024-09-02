from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Initialize empty list to store prefixes
    prefixes = []

    # Get all prefixes from the input string
    for prefix in re.findall(r'^[a-zA-Z]+', string):
        prefixes.extend(prefix for prefix in re.findall(r'^[a-zA-Z]+', prefix) if prefix != prefix[0])

    # Sort prefixes
    prefixes = sorted(prefixes)

    # Return prefixes
    return prefixes

