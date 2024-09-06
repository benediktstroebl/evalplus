from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = ["".join(string)]
    string_length = len(string)
    for i in range(string_length):
        string = string[:i + 1]
        prefixes.append(string)
    return prefixes[::-1]

