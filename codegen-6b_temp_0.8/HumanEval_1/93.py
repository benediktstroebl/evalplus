from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = [('(', ')')]
    final_list = []
    for char in paren_string:
        if char == '(':
            stack.append(('(', ')'))
        elif char == ')':
            pair = stack.pop()
            if pair[0] != pair[1]:
                return "Invalid string"
        elif char != ' ':
            final_list.append(char)
    return final_list

