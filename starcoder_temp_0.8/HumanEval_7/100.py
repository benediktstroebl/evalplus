from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    # solution without recursion
    # return [x for x in strings if substring in x]

    # solution with recursion
    if len(strings) == 0:
        return []
    else:
        # base case
        if substring in strings[0]:
            return [strings[0]]
        # recursive case
        else:
            return filter_by_substring(strings[1:], substring) + filter_by_substring(strings[1:], substring)

