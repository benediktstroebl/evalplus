from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if not paren_string:
        return []
    if paren_string[0]!= '(' or paren_string[-1]!= ')':
        return []
    stack = [paren_string[0]]
    ret = []
    for i in range(1, len(paren_string)):
        if stack and paren_string[i] == ')' and stack[-1] == '(':
            ret.append(''.join(stack[1:-1]))
            stack = []
        stack.append(paren_string[i])
    return ret
