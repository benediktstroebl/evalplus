from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    index = 0
    stack = [0]
    paren_groups = []
    while index < len(paren_string):
        if paren_string[index] == '(':
            stack.append(index)
        elif paren_string[index] == ')':
            start = stack.pop()
            end = index
            paren_groups.append(paren_string[start + 1:end])
        index += 1
    return paren_groups

