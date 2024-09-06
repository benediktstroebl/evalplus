from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    else:
        max_idx = strings[0].index(max(strings[0], key=len))
        return strings[max(strings[0].startswith(strings[1]), strings[1].startswith(strings[0]))][:max_idx+1]