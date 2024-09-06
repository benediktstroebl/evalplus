from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if not paren_string:
        return []
    open_parens_left, open_parens_right, current_group = 0, 0, ""
    paren_groups = []
    for char in paren_string:
        if char == '(':
            open_parens_left += 1
        elif char == ')':
            open_parens_right += 1
        if open_parens_left == open_parens_right:
            current_group += char
            paren_groups.append(current_group)
            open_parens_right, current_group = 0, ""
    return paren_groups

