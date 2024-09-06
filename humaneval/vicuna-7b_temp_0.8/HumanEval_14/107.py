from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    current = ""
    for i in range(len(string)):
        if string[i] == string[i+1]:
            current += string[i]
        else:
            prefixes.append(current)
            current = string[i]
    prefixes.append(current)
    return prefixes