from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    group_stack = []
    for paren in paren_string:
        if paren == "(":
            group_stack.append(paren)
        elif paren == ")":
            if group_stack:
                group_stack.pop()
            else:
                return group_stack
    return group_
