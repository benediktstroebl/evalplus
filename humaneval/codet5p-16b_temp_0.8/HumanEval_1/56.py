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
    open_parens = []
    open_parens_count = 0

    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            open_parens.append(paren_string[i])
            open_parens_count += 1
        elif paren_string[i] == ')':
            open_parens.pop()
            open_parens_count -= 1
        elif paren_string[i] =='' and open_parens_count == 0:
            result.append(''.join(open_parens))
            open_parens = []

    return result

