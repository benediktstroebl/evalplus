from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    # make sure the list is not empty
    if len(strings) == 0:
        return None

    # find the first string in the list
    longest_string = strings[0]

    # for each string in the list
    for string in strings:
        # if the string is longer than the current one
        if len(string) > len(longest_string):
            # set the string as the new longest string
            longest_string = string

    # return the longest string
    return longest_string


