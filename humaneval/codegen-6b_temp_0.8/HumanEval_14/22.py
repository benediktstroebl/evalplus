from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    shortest_len = len(string)
    list_of_chars = [string[:i] for i in range(1, shortest_len + 1)]
    return list_of_chars

