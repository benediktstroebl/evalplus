from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_stack: List[str] = []
    group_stack: List[str] = []
    for index, item in enumerate(paren_string):
        if item == '(':
            paren_stack.append(index)
        elif item == ')':
            if not paren_stack:
                raise ValueError('Parentheses are not balanced')
            paren_index = paren_stack.pop()
            group_stack.append(paren_string[paren_index: index + 1])
    return group_stack

