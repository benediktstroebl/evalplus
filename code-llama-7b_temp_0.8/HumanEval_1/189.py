from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack: List[str] = []
    groups: List[str] = []
    for i, char in enumerate(paren_string):
        if char == '(':
            stack.append('(')
        elif char == ')':
            if not stack:
                raise Exception(f'Unmatched right parenthesis at {i + 1}')
            stack.pop()
        else:
            continue
        if not stack:
            groups.append(''.join(stack))
            stack.clear()
    if stack:
        raise Exception(f'Unmatched left parenthesis at {len(paren_string)}')
    return groups

