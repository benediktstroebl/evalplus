from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string_chars = set(string)
    prefixes = []
    for prefix in string_chars:
        prefixes.extend(string_chars - set([''.join(filter(str.isalpha, prefix))]))
    return sorted(prefixes, reverse=True)

