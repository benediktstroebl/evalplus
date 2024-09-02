from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    result = []
    current = ''
    for prefix in string:
        if current == '':
            result.append(prefix)
            current = prefix
        else:
            result.append(current)
            current = prefix
    if current == '':
        result.append(current)
    return result

