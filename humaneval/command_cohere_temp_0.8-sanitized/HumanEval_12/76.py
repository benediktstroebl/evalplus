from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_string = max(strings, key=len)  # Get the longest string
    if len(set(strings)) == 1:  # If there's only one string of that length
        return longest_string
    return longest.func_1(strings, longest_string)
def func_1(strings: List[str], current: str) -> str:
    return current