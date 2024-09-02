from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    if len(string) == 1:
        return [string]
    elif len(string) == 0:
        return []
    else:
        prefixes = []
        prefixes.append(string)
        prefixes.append(string[0:1])
        prefixes.extend(all_prefixes(string[1:]))
        return prefixes

