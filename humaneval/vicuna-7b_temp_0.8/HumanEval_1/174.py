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
    stack = [paren_string]
    for open_brace in stack:
        if open_brace == '(':
            result.append(open_brace)
            stack.append(')')
        elif open_brace == ')':
            result.append(open_brace)
            stack.pop()
        elif open_brace in stack:
            while stack[-1] != ')' and stack[-1] != '(':
                stack.pop()
            stack.pop()
    if stack:
        result.append(stack.pop())
    return result

