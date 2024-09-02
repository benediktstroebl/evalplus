from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if not paren_string:
        return []
    output = []
    for i in range(1, len(paren_string)):
        if paren_string[i] == '(':
            output.append('')
        elif paren_string[i - 1] == '(' and paren_string[i] == ')':
            output[-1] += paren_string[i]
        else:
            output[-1] += paren_string[i]

    return output

