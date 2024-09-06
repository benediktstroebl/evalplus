from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    length = len(string)
    substr = ""
    result = []
    for i in range(length):
        substr += string[i]
        result.append(substr)
    return result

