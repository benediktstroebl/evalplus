from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """
    Return the length of the longest string in the list.
    """
    # Initialize the max length to 0
    max_length = 0
    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
    return max_length