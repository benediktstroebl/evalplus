from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    groups = []
    stack = []

    for i, x in enumerate(paren_string):
        if x == "(":
            stack.append(x)
        else:
            if len(stack) > 0 and stack[-1] == "(":
                groups.append("".join(stack))
                stack.pop()
            else:
                stack.append(x)

    while len(stack) > 0:
        if stack[-1] == "(":
            stack.pop()
        else:
            groups.append("".join(stack))

    
