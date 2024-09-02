from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    result = []
    for prefix in string.split(''):
        prefix_len = len(prefix)
        result.extend(prefix_len, prefix)
    result = sorted(result)
    return result

