from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Naive approach:
    # all_prefixes = []
    # for i in range(len(string)+1):
    #     all_prefixes.append(string[:i])
    # return all_prefixes

    # Alternate approach:
    # all_prefixes = []
    # for i in range(len(string), -1, -1):
    #     all_prefixes.append(string[:i])
    # return all_prefixes

    # Better approach:
    all_prefixes = [string[:i] for i in range(len(string)+1)]
    return all_prefixes

