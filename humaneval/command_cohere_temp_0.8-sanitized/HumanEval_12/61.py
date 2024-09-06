from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    :param strings: List of strings.
    :return: Longest string or None.
    """
    # Ensure we have at least one string to work with
    if not strings:
        return None

    # Use a loop to find the longest string
    max_length = 0
    longest_str = None
    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
            longest_str = string
        elif len(string) == max_length:
            longest_str = string

    return longest_str