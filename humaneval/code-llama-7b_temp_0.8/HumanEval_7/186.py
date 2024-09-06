from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    # check that 'strings' is not None
    assert strings is not None, "Input strings cannot be None"
    # check that 'substring' is not None
    assert substring is not None, "Input substring cannot be None"

    # define a list to hold all the elements from the input list 'strings' that contain 'substring'
    filtered_strings = []

    # for each element in 'strings', check if it contains the 'substring'
    for string in strings:
        if substring in string:
            filtered_strings.append(string)

    return filtered_strings

