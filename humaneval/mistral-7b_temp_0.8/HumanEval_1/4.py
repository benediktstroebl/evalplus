from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    parentheses = []
    stack = []
    # open or close parentheses
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                parentheses.append('')
                continue
            # peek to check if open parentheses is balanced
            open_parentheses = stack.pop()
            if open_parentheses == '(':
                parentheses.append(parentheses.pop() + char)
            else:
                parentheses.append(char)
    return parentheses

