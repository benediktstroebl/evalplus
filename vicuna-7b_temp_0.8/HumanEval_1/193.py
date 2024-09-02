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
    current_depth = 0
    for char in paren_string:
        if char == '(':
            current_depth += 1
            stack.append(current_depth)
        elif char == ')':
            current_depth -= 1
            while stack[-1] != current_depth:
                stack.pop()
            result.append(stack.pop())
        elif char == ' ':
            pass
    return result
