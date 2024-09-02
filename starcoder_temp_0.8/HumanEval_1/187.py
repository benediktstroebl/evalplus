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
    result = []
    for letter in paren_string:
        if letter == "(":
            stack.append(letter)
        elif letter == ")":
            if not stack:
                stack.append(letter)
            else:
                stack.pop()
            if not stack:
                result.append("")
    if stack:
        result[-1] += stack.pop()
    return result

