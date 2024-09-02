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
    res = []
    for char in paren_string:
        if char == '(':
            if not stack:
                stack.append(('T', ''))
            current_stack = stack[-1]
            stack.append((' ', ''))
        elif char == ')':
            if not current_stack:
                res.append('')
            else:
                current_stack = current_stack[::-1]
                if not current_stack:
                    res.append('')
                else:
                    current_stack[-1] = current_stack[-1] + ')'
                stack.pop()
        else:
            current_char = char
            while current_char == ' ':
                current_char = paren_string[stack[-1][1]:stack[0][0]].strip()
                stack.pop()
            current_stack.append(current_char)
    return res

