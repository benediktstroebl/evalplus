from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_stack = []
    result = []
    for i in range(len(paren_string)):
        if paren_string[i] == "(":
            paren_stack.append(paren_string[i])
        elif paren_string[i] == ")":
            while paren_stack[-1] != "(":
                result.append(paren_stack.pop())
            paren_stack.pop()
        elif paren_string[i] == " ":
            pass
        else:
            while len(paren_stack) > 0 and paren_stack[-1] != "(":
                result.append(paren_stack.pop())
            paren_stack.append(paren_string[i])
    while len(paren_stack) > 0:
        result.append(paren_stack.pop())
    return result

