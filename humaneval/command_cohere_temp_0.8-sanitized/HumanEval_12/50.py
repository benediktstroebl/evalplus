from typing import List, Optional
import unittest
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    
    :param strings: List of strings.
    :return: Longest string or None.
    """
    # Check if the list is empty
    if not strings:
        return None
    
    # Initialize the result
    longest_str = strings[0]
    
    # Check for other strings of the same length and update if needed
    for strng in strings:
        if len(strng) > len(longest_str):
            longest_str = strng
    
    return longest_str