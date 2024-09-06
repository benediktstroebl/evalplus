from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    prefixes = []
    if len(string) > 0:
        prefixes.append(string)
        prefixes.append(string[0])
        all_prefixes(string[1:])

    return prefixes
