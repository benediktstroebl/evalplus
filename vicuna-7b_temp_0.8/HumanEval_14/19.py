from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # convert string to list of characters
    string_chars = string.split()
    # create an empty list to store prefixes
    prefixes = []
    # iterate through each character in the string_chars
    for char in string_chars:
        # add the prefix to the list if it's a prefix of the input string
        prefixes.append(char)
        # if the current character is not a prefix of the input string
        # it means the input string has a prefix that is longer than the current character
        # so we can add all prefixes of the input string up to this character
        for prefix in prefixes:
            prefixes.extend(string_chars[:prefix])
        # clear the prefixes list so we can start with the next character
        prefixes = []
    return prefixes

