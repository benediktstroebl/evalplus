from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string = str(string)
    prefixes = []
    for prefix in string:
        prefix_len = len(prefix)
        for i in range(prefix_len, len(string)):
            prefixes.append(string[i:])
        prefixes.append(prefix)
    prefixes.reverse()
    return prefixes