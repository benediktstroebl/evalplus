from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    result = []
    for prefix in string.split(''):
        prefix_length = len(prefix)
        for i in range(prefix_length, len(string)):
            result.append(string[i-prefix_length:i])
    return result

