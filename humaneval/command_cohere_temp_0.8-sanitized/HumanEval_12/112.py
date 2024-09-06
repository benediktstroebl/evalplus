from typing import List, Optional
import unittest
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    :param strings: List of strings.
    :return: Longest string.
    """
    # Sorting the list of strings by their length, ascending.
    # This way, the longest string will be at the end of the list.
    strings.sort(key=len, reverse=True)
    return strings[0] if strings else None