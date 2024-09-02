from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string_chunks = string.split()
    prefixes = []
    for i, chunk in enumerate(string_chunks):
        prefixes.append(chunk)
        if i == len(string_chunks) - 1:
            prefixes.append(string_chunks[i:])
    return prefixes

