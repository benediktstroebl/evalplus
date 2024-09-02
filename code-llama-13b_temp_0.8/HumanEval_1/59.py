from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_stack = []
    open_paren_indexes = []
    for i, char in enumerate(paren_string):
        if char == '(':
            open_paren_indexes.append(i)
        if char == ')':
            start_idx = open_paren_indexes.pop()
            paren_stack.append((start_idx, i))
    return [paren_string[s:e + 1] for s, e in paren_stack]

