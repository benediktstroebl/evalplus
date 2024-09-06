from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string = string.strip()
    prefixes = [string[0]]
    for index, char in enumerate(string[1:], start=1):
        prefixes.append(string[:index])
    return prefix
