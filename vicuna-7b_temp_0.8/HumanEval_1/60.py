from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = [paren_string]
    result = []
    while stack:
        curr_stack = stack.pop()
        if curr_stack == '':
            continue
        if curr_stack == '(':
            stack.append(curr_stack)
            result.append(curr_stack)
        elif curr_stack == ')':
            if not stack or stack[-1] != '(':
                break
            stack.pop()
            result.append(stack.pop())
    return result

