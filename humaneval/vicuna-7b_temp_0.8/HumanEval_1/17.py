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
    open_brace_count = 0
    result = []
    for char in paren_string:
        if char == '(':
            stack.append(char)
            open_brace_count += 1
        elif char == ')':
            if not stack or stack[-1] != '(':
                raise ValueError("Unbalanced parentheses")
            stack.pop()
            open_brace_count -= 1
        elif char == ' ':
            pass
        elif char == '}':
            if not open_brace_count:
                raise ValueError("Unmatched closing brace")
            stack.pop()
            open_brace_count -= 1

    result.extend(stack)
    return result

