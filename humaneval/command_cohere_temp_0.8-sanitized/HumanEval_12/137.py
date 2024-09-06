from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_string = max(strings, key=len)  # Get the longest string
    if len(set(strings)) == 1:  # If there is only one string of that length
        return longest_string
    return longest_string[0]  # Return the first one in case of multiple strings of the same length