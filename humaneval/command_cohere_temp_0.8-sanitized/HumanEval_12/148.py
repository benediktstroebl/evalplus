def longest(strings: List[str]) -> Optional[str]:
    # Type hinting
    from typing import List, Optional

    # If the list is empty return None
    if not strings:
        return None
    # If there is only one string return it
    if len(strings) == 1:
        return strings[0]
    # If there is more than one string, return the longest one
    return max(strings, key=len)