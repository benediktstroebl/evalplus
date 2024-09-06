from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_string = max(strings, key=len)
    return longest_string if len(longest_string) == max(len(s) for s in strings) else longest(
        [s for s in strings if s != longest_string]
    )