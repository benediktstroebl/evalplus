from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_stack = []
    group_stack = []
    current_group = ""
    for char in paren_string:
        if char == "(":
            paren_stack.append(char)
        elif char == ")":
            if len(paren_stack) > 0:
                paren_stack.pop()
                current_group += char
            else:
                group_stack.append(current_group)
                current_group = char
        else:
            if len(paren_stack) > 0:
                current_group += char

    return group_stack

