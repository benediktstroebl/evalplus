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
    brace_stack = []
    cur_pos = 0
    while cur_pos < len(paren_string):
        char = paren_string[cur_pos]
        if char == '(':
            brace_stack.append(char)
        elif char == ')':
            if len(brace_stack) == 0:
                raise Exception("Parens are not balanced")
            brace_stack.pop()
        elif char == ' ':
            pass
        else:
            raise Exception("Parens are not separated")
        cur_pos += 1
    if len(brace_stack) == 0:
        result = paren_string.split()
    else:
        raise Exception("Parens are not balanced")
    return result

