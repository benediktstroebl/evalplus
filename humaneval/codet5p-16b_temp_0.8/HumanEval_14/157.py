from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    all_prefixes_list = []
    for i in range(len(string) + 1):
        all_prefixes_list.append(string[0:i])
    return all_prefixes_list

