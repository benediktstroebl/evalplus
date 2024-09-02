from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    paren_groups = []
    paren_stack = []
    start_pos = 0
    while start_pos < len(paren_string):
        end_pos = len(paren_string)
        if paren_string[start_pos] == '(':
            paren_stack.append('(')
        elif paren_string[start_pos] == ')':
            paren_stack.pop()
            if paren_stack:
                end_pos = start_pos + 1
            else:
                paren_groups.append(paren_string[start_pos:end_pos])
                start_pos = end_pos
    return paren_groups

