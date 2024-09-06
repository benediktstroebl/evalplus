from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    stack = []
    try:
        for i, c in enumerate(paren_string):
            if c == '(':
                stack.append(i)
            elif c == ')' and stack:
                result.append(paren_string[stack.pop() + 1:i])
    except IndexError:
        pass
    return result
