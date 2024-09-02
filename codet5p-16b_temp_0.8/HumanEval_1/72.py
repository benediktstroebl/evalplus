from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if paren_string.count('(') == paren_string.count(')'):
        return [paren_string]
    open_parens = [i for i, char in enumerate(paren_string) if char == '(']
    close_parens = [i for i, char in enumerate(paren_string) if char == ')']
    for i, _ in enumerate(open_parens):
        for j, _ in enumerate(close_parens):
            if open_parens[i] < close_parens[j]:
                break
        else:
            continue
        break
    separate_groups = separate_paren_groups(paren_string[:open_parens[i]]) + \
                      separate_paren_groups(paren_string[close_parens[j] + 1:])
    return separate_groups

