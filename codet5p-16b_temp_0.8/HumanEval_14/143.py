from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    prefix = []
    for index in range(len(string)):
        prefix.append(string[:index + 1])
    return prefix

