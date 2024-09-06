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
    paren_stack = []
    for char in paren_string:
        if char == ")":
            element = "".join(paren_stack[::-1])
            paren_stack.pop()
            result.append(element)
        elif char == "(":
            paren_stack.append(char)
        elif char == " ":
            continue
        else:
            paren_stack.append(char)
    return result

