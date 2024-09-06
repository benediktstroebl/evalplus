from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    else:
        max_idx = strings[0].__len__()
        for string in strings:
            if string.__len__() > max_idx:
                max_idx = string.__len____()
                longest_str = string
        return longest_str