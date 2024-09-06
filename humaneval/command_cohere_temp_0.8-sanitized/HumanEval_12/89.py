from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    longest_idx = max(range(len(strings)), key=lambda idx: len(strings[idx]))
    return strings[longest_idx]