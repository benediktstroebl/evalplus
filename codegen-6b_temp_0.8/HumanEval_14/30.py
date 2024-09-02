from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    if not string:
        return ['']

    return [''.join(i for i in string)] + [prefix + string[1:] for prefix in all_prefixes(string[1:])]

