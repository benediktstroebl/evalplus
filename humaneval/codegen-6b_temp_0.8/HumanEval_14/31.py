from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    start = 0
    result = [string[:start + 1]]
    while start < len(string) - 1:
        start += 1
        result.append(string[:start + 1])
    return result

