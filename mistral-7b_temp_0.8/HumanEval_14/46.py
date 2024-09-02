from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = ["" + s for s in string]
    for i in range(1, len(string) + 1):
        prefixes.append(prefixes[i - 1] + string[i - 1])
    return prefixes
