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
    last_index = 0
    paren_group_strings = []
    for i, char in enumerate(paren_string):
        if char == '(':
            paren_stack.append(i)
        if char == ')':
            paren_stack.pop()
        if not paren_stack:
            paren_group_strings.append(paren_string[last_index:i + 1])
            last_index = i + 1
    return paren_group_strings

