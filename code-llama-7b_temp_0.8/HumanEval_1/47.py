from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result: List[str] = []
    stack: List[str] = []
    for char in paren_string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if stack:
                stack.pop()
            else:
                result.append("" if not result else result[-1] + ")")
    if stack:
        raise ValueError("unbalanced parenthesis")
    return [part if not result else result[-1] + part for part in result + [stack[0] + ")" * len(stack)]]

