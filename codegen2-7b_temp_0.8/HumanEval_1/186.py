from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    open_paren = '('
    close_paren = ')'
    bracket_strings = []
    for paren in paren_string:
        if paren == open_paren:
            bracket_strings.append(open_paren)
        elif paren == close_paren:
            if not bracket_strings:
                return []
            bracket_strings.pop()
    return bracket_strings
