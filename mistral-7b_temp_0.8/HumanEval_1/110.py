from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    bracket_string_list = []
    bracket_stack = []
    for bracket in paren_string:
        if bracket == '(':
            bracket_stack.append(bracket)
        elif bracket == ')':
            bracket_string_list.append(''.join(bracket_stack))
            bracket_stack = []
    if bracket_string_list:
        bracket_string_list.append(''.join(bracket_stack))
    return bracket_string_list

