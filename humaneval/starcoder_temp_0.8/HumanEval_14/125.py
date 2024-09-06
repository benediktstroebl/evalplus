from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    if string == "":
        return []

    first_char = string[0]
    first_prefix = [first_char]

    rest_prefixes = all_prefixes(string[1:])

    return first_prefix + rest_prefixes

