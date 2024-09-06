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
    result = []
    for char in paren_string:
        if char == '(':
            if current_group:
                current_group.pop()
                stack.pop()
            stack.append(current_group.pop())
            current_group.append('(')
        elif char == ')':
            if not current_group or current_group[-1] != '(':
                current_group.pop()
                stack.pop()
            else:
                current_group.pop()
                stack.pop()
        else:
            current_group.append(char)
    for item in stack:
        result.append(item)
    return result

