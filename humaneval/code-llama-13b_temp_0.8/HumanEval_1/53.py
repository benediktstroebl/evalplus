from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # HINT: use stack to maintain the state
    stack = []
    result = []
    for ch in paren_string:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if len(stack) > 0:
                stack.pop()
                if len(stack) == 0:
                    result.append(')')
            else:
                stack.append(ch)
    return ['(' + ''.join(result) for result in result]

