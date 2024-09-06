from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    temp = ''
    bracket_stack = []
    for character in paren_string:
        if character == '(':
            bracket_stack.append('(')
        elif character == ')':
            if len(bracket_stack) != 0:
                bracket_stack.pop()
        temp += character
        if len(bracket_stack) == 0 and character == ')':
            result.append(temp)
            temp = ''
    return result

