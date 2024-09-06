from typing import List, Optional
import unittest
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    :param strings: List of strings.
    :return: Longest string or None.
    """
    # Check for empty list
    if not strings:
        return None
    
    # Use a variable to track the maximum length and the corresponding element.
    longest_len = 0
    longest_str = None
    
    # Iterate through the list and update the variables as needed.
    for str_ in strings:
        if len(str_) > longest_len:
            longest_len = len(str_)
            longest_str = str_
    
    return longest_str