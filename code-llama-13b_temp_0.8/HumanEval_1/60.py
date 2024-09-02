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
    result = []
    stack = []
    i = 0
    while i < len(paren_string):
        if paren_string[i] == "(":
            stack.append(i)
        elif paren_string[i] == ")":
            if len(stack) == 0:
                raise ValueError("The parentheses are not balanced")
            else:
                open_index = stack.pop()
                result.append(paren_string[open_index:i + 1])
        i += 1
    if len(stack) != 0:
        raise ValueError("The parentheses are not balanced")
    return result

