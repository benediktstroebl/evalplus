from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_string = max(strings, key=len)
    return longest_string if len(set(strings).count(longest_string)) == 1 else longest_search_secondary_longest(strings)
def longest_search_secondary_longest(strings: List[str]) -> str:
    longest_secondary = max(strings, key=len)
    return longest_secondary if len(set(strings).count(longest_secondary)) == 1 else longest_search_secondary_longest(strings)