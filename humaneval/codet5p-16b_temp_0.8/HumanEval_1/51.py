from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    print(paren_string)
    open_parens = []
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            open_parens.append(i)
        elif paren_string[i] == ')':
            open_parens.pop()

    print(open_parens)
    results = []
    for j in range(len(open_parens)):
        results.append(paren_string[open_parens[j] + 1: open_parens[j + 1]])
    return results

