from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(" ", "")
    stack = []
    paren_groups = []

    for character in paren_string:
        if character == "(" or character == ")":
            if not stack:
                stack.append(character)
            else:
                if not stack[-1] == "(":
                    stack.pop()
                else:
                    stack.pop()
                    paren_groups.append("".join(stack))
                    stack = []
        else:
            stack.append(character)
    return paren_
