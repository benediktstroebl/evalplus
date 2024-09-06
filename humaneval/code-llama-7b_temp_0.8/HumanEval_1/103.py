from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack: List[str] = []
    result: List[str] = []
    for char in paren_string:
        if char == "(":
            stack.append("(")
        elif char == ")":
            if len(stack) > 0:
                stack.pop()
            else:
                result.append("(")
        else:
            if len(stack) > 0:
                result[-1] += char
            else:
                result.append(char)
    return result + stack[::-1]

