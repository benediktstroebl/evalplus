from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longestStr = max(strings, key=len)
    return longestStr if len(longestStr) == max(len(s) for s in strings) else longest(strings[:strings.index(longestStr)])