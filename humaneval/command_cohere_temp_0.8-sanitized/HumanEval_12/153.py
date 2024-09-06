from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_string = max(strings, key=len)  # Get the longest string
    if len(set(strings)) == 1:  # If there is only one string of that length
        return longest_string
    return longest.func_first_occurrence(longest_string, strings)
def func_first_occurrence(longest_string, strings):
    return next((s for s in strings if s == longest_string), strings[0])