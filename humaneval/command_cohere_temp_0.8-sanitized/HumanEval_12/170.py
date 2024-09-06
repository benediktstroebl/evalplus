from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longestStr = max(strings, key=len)
    return longestStr if len(longestStr) == max(map(len, strings)) else longest(list(filter(lambda x: x == longestStr, strings)))