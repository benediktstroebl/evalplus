from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    all_prefixes_list = []
    all_prefixes_list.append('')
    for i in range(len(string)):
        for j in range(i + 1):
            all_prefixes_list.append(string[j:i + 1])
    return all_prefixes_list

