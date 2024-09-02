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
    groups = []
    for i, c in enumerate(paren_string):
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                raise Exception("Unbalanced parens at index {0}".format(i))
            stack.pop()
            groups.append(paren_string[i + 1:])
    if stack:
        raise Exception("Unbalanced parens at end")

    return groups

