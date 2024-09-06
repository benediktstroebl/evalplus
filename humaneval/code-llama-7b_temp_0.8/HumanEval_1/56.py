from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    list_of_groups = []
    paren_stack = []
    paren_group = ''
    for paren in paren_string:
        if paren == '(':
            paren_stack.append(paren)
            paren_group += paren
        elif paren == ')':
            if len(paren_stack) == 0:
                return list_of_groups
            elif paren_stack[-1] == '(':
                paren_stack.pop()
                paren_group += paren
                list_of_groups.append(paren_group)
                paren_group = ''
            else:
                return list_of_groups
    return list_of_groups

