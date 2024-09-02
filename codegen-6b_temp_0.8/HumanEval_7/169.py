from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    if (substring[0] != ".") and (substring[0] != "?") and (substring[0] != "-") and (substring[0] != "_"):
        raise ValueError('Given substring must have a single character between being \"?\" or \"-\" or \"_\"')

    if len(substring) > 1:
        raise ValueError('Given substring must have a single character between being \"?\" or \"-\" or \"_\"')

    filtered = []
    for string in strings:
        if substring in string:
            filtered.append(string)

    return filtered

