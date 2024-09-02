from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = []
    current_group = []
    for char in paren_string:
        if char == '(':
            if not current_group or current_group[-1] != ')':
                stack.append(current_group)
                current_group = [']']
            current_group.append(char)
        elif char == ')':
            if not current_group:
                return []
            group_string = ''.join(current_group)
            current_group = stack.pop()
            if group_string == '':
                return []
            return [group_string]
