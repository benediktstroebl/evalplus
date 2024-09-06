from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string = string.lower()
    string = string.split()
    string = [str(i[0]) +'' for i in string]
    string = [s for s in string if s!= '']
    return sorted(string, key=len)
