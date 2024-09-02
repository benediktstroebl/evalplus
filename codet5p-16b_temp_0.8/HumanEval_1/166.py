from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    paren_string = paren_string.replace(' ', '')
    group_list = []
    group_stack = []

    for char in paren_string:
        if char == '(':
            group_stack.append(char)
        if char == ')':
            if len(group_stack) == 0:
                raise Exception('No group to close')
            last_opened = group_stack.pop()
            if last_opened == '(':
                group_list.append(''.join(group_stack))
                group_stack = []
            else:
                group_stack.append(last_opened)

    if len(group_stack) > 0:
        raise Exception('No group to close')

    return group_list

