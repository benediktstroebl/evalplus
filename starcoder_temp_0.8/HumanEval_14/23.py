from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefix = [""]
    for char in string:
        prefix.append(prefix[-1] + char)
    return prefix
