from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    result = []
    for prefix in get_prefixes(string):
        prefix_length = len(prefix)
        start = 0
        while start < len(string) and string[start:start+prefix_length] == prefix:
            start += prefix_length
        result.append(prefix)
    return result
