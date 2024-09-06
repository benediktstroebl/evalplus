from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    count_open_braces = 0
    stack_parens: List[str] = []
    ret = []

    for c in paren_string:
        if c == '(':
            count_open_braces += 1
        elif c == ')':
            if count_open_braces:
                count_open_braces -= 1
            else:
                ret.append(''.join(stack_parens))
                stack_parens = []
        else:
            if count_open_braces:
                stack_parens.append(c)
            else:
                ret.append(c)

    if count_open_braces:
        ret.append(''.join(stack_parens))
    return ret

