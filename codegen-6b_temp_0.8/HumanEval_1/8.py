from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    start_index = 0
    results = []
    while start_index < len(paren_string):
        end_index = find_matching_paren(paren_string, start_index)
        if end_index == -1:  # no matching paren, so add remainder of input
            results.append(paren_string[start_index:])
            break
        else:
            results.append(paren_string[start_index:end_index + 1])
            start_index = end_index + 1
    return results

