from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    stack = []
    for paren in paren_string:
        if paren == '(':
            stack.append(paren)
        elif paren == ')':
            if len(stack) == 0:
                raise ValueError(f"Invalid parentheses {paren}")
            stack.pop()

    if len(stack)!= 0:
        raise ValueError(f"Unmatched parentheses {stack}")

    return [paren_group[1:-1] for paren_group in paren_string.split(')(') if paren_group]

