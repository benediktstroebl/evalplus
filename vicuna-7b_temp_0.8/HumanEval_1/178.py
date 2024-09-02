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
    open_pairs = 0
    result = []
    for char in paren_string:
        if char == '(':
            stack.append('(')
            open_pairs += 1
        elif char == ')':
            stack.pop()
            if not stack or stack[-1] != '(':
                raise ValueError
            open_pairs -= 1
        elif open_pairs == 0:
            result.append(stack.pop())
            open_pairs = stack.pop()
    result.extend(stack)
    return result
