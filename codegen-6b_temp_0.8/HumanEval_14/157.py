from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    ls, res = [], []
    for i in range(1, len(string)+1):
        ls.append(string[:i])
    for i in ls:
        if i not in res:
            res.append(i)
    return res

