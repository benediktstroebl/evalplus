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
    groups = []
    for char in paren_string:
        if char == '(':
            group_stack.append(char)
        if char == ')':
            if len(group_stack)!= 0 and group_stack[-1] == '(':
                group_stack.pop()
            else:
                groups.append(''.join(group_stack))
                group_stack = []
    if len(group_stack)!= 0:
        groups.append(''.join(group_stack))
    return groups
