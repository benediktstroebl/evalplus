from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    parens = [paren for paren in paren_string if paren in '{[(']
    current_string = ''
    stack = []
    for paren in parens:
        if paren in '{[(':
            stack.append(paren)
        else:
            if stack:
                stack_top = stack.pop()
                if (stack_top, paren) == ('(', ')') or (stack_top, paren) == ('[', ']') or (stack_top, paren) == (
                        '{', '}'):
                    current_string += stack_top + paren
                else:
                    current_string += '{}{}'.format(stack_top, paren)
            else:
                current_string += paren
    return current_string.split(sep=' ')

