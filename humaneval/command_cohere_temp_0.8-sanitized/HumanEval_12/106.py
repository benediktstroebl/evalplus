from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    
    :param strings: List of strings.
    :return: Longest string.
    """
    # Check if the list is empty
    if not strings:
        return None
    
    # Initialize variables to track the longest string and its index.
    max_length = 0
    longest_str = None
    index = -1
    
    # Iterate through the list and find the longest string.
    for i, string in enumerate(strings):
        if len(string) > max_length:
            max_length = len(string)
            longest_str = string
            index = i

    # Return the longest string or the first one if multiple strings have the same length.
    return longest_str if longest_str and index != -1 else strings[0]