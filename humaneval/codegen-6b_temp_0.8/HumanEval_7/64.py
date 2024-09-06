from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    substring_index = 0
    while substring_index < len(substring):
        for string in strings:
            if substring[substring_index] in string:
                substring_index += 1
                continue
            else:
                strings.remove(string)
    return strings

