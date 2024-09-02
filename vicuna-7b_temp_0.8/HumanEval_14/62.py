from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Store all characters in a set, since it is more efficient than a list for this purpose
    # and we don't need to worry about duplicates
    characters = set(string)

    # Create an empty list to store prefixes
    prefixes = []

    # Start by adding the longest prefix
    prefixes.append(string)

    # Loop through all characters in the set, checking if they are still unused
    for char in characters:
        # If the character is already in the list of prefixes, we can't use it
        if char in prefixes:
            continue

        # If the character is in the set but not in the list of prefixes, it is a new prefix
        prefixes.append(char)

    # Reverse the order of the prefixes
    prefixes = list(reversed(prefixes))

    return prefixes

