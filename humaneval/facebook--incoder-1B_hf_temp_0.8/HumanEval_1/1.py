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
    parens = paren_string.split(")")
    paren_groups = []
    paren_stack = []
    parens_open = True
    parens_closed = True
    for paren in parens:
        if parens_open:
            if paren not in paren_stack:
                paren_groups.append(paren)
                parens_open = False
            if parens_closed:
                if paren not in paren_stack:
                    paren_groups.append(paren)
                    parens_closed = False
        else:
            if paren not in paren_stack:
                paren_stack.append(paren)
            if paren not in paren_stack:
                paren_groups.append(paren)
                parens_closed = False
    return paren_groups

