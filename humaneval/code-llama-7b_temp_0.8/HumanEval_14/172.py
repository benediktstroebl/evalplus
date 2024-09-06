from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    if len(string) == 0:
        return []
    if len(string) == 1:
        return [string]
    prefix_list = [string[0]]
    for i in range(1, len(string)):
        prefix_list.append(prefix_list[i - 1] + string[i])
    return prefix_list

