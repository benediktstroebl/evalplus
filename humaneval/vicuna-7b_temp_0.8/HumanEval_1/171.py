from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    nested_parens = 0
    paren_stack = [paren_string]
    result = []

    while paren_stack:
        curr_paren = paren_stack[-1]
        if curr_paren == '(':
            nested_parens += 1
        elif curr_paren == ')':
            nested_parens -= 1

        if nested_parens == 0:
            result.append(paren_stack.pop())

        paren_stack.append(curr_paren)

    return result

