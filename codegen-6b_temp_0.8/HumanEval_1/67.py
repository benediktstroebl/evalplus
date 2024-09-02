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
    i = 0
    while i < len(paren_string):
        if paren_string[i] == "(":
            stack.append(i)
        elif paren_string[i] == ")" and len(stack) > 0:
            groups.append(paren_string[stack.pop() + 1 : i])
        i += 1
    groups.reverse()
    return groups

