from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    assert len(string) > 0, "Cannot have a zero length string"
    return [string[:i] for i in range(len(string)+1)]
