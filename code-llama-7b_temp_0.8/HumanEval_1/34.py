from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    num_open = 0
    paren_group = ""
    paren_groups = []

    for char in paren_string:
        if char == '(':
            num_open += 1
            paren_group += '('
        elif char == ')':
            num_open -= 1
            paren_group += ')'
            if num_open == 0:
                paren_groups.append(paren_group)
                paren_group = ""
        else:
            paren_group += char
    return paren_groups

