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
    for char in paren_string:
        if char == '(':
            stack.append('(')
            result.append(stack.pop())
        elif char == ')':
            stack.append(')')
            result.append(stack.pop())
        elif char == ' ':
            # ignore space
            pass
        else:
            if not stack or (char != stack[-1] and char != '(' and char != ')') and char != '[' and char != ']':
                # not balanced or nested
                stack.append(char)
        if len(stack) == 0:
            while '(' in result[-1]:
                result.pop()
    return result