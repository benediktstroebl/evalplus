from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    # start with an empty list
    result = []
    # run a for-loop from 0 to the length of the strings
    for i in range(len(strings)):
        # check if the string starts with the prefix
        if strings[i].startswith(prefix):
            # add the string to the list
            result.append(strings[i])
    # return the list
    return result

