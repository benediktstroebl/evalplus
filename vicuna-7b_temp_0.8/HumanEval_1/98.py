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
    open_brace_count = 0
    for char in paren_string:
        if char == '(':
            stack.append('(')
            open_brace_count += 1
        elif char == ')':
            stack.append(')')
            open_brace_count -= 1
            if open_brace_count == 0:
                result.append(stack.pop())
        elif char == ' ':
            pass
        else:
            if not stack:
                raise ValueError('Unbalanced parentheses')
            else:
                stack[-1] += char
    return result

