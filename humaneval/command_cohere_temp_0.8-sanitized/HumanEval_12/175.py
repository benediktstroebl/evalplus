from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    longest_str = max(strings, key=len)
    return longest_str