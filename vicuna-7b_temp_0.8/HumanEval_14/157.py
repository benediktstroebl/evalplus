from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string_list = list(string)
    prefixes = []
    for prefix in string_list:
        prefixes.extend(string_list[i:j] for i, j in zip([0] + string_list[:-1], string_list))
        prefixes.reverse()
    return prefixes