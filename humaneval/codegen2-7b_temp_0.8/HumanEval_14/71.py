from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    if not string:
        return []

    pre = [string[0]]
    for i in range(len(string)):
        pre.append(pre[-1][:i + 1])

    return pre
