from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    open_paren = '('
    close_paren = ')'
    stack = []
    output = []
    for char in paren_string:
        if char == open_paren:
            stack.append(char)
        elif char == close_paren:
            if not stack:
                return []
            elif stack[-1] == open_paren:
                stack.pop()
                if not stack:
                    output.append(paren_string[:len(stack) + 1])
                    paren_string = paren_string[len(stack) + 1:]
            else:
                return []

    if stack:
        return []
    else:
        return output

