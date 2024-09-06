from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # positive - means parenthesis is open
    # negative - means parenthesis is closed
    # 0 - means parenthesis is balanced
    stack = []
    temp_str = ""
    paren_groups = []
    for c in paren_string:
        if c == " ":
            continue
        if c == "(":
            stack.append(1)
        elif c == ")":
            stack.pop()
        temp_str += c
        if not stack:
            paren_groups.append(temp_str)
            temp_str = ""
    return paren_groups

