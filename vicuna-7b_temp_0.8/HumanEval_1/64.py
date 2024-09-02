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
    current_len = 0
    for char in paren_string:
        if char == '(':
            stack.append(current_len)
            current_len += 1
        elif char == ')':
            current_len -= 1
            if current_len == -1:
                # remove last empty group
                stack.pop()
            else:
                result = ''.join(stack)
                stack = [''] * current_len
                stack.append(result)
                current_len = 0
        elif char == ' ':
            pass
    # remove last empty group
    stack.pop()
    return list(stack)

