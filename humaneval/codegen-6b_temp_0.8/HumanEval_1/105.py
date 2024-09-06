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
    brackets = []
    for paren in paren_string:
        if paren == '(':
            paren_stack.append(paren)
        elif paren == ')':
            brackets.append(paren_stack.pop())
        elif not paren_stack and paren in '()':
            brackets.append(paren)

    if paren_stack:
        raise ValueError('Unbalanced parentheses')

    return_list = []
    for open_bracket, close_bracket in zip(brackets[::2], brackets[1::2]):
        if open_bracket == '(':
            return_list.append(close_bracket)
        else:
            return_list.append(open_bracket)
    return return_list

