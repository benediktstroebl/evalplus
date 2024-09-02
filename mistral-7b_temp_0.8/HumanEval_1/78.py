from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    current_list = []
    current_str = ''
    stack = []

    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                current_list.append(current_str)
                current_str = ''
            else:
                current_str += char
                stack.pop()
        else:
            current_str += char

    if current_str:
        current_list.append(current_str)

    return current_list

