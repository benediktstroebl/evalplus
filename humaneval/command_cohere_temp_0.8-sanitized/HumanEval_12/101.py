from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Return the longest string in a list of strings, or None if the list is empty. In case of
    multiple longest strings, return the first one. 
    """
    if not strings:
        return None
    longest_string = max(strings, key=len)
    return longest_string