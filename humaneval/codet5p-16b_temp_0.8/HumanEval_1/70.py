from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    open_braces = ['(', '[', '{']
    close_braces = [')', ']', '}']
    stack = []
    for i, c in enumerate(paren_string):
        if c in open_braces:
            stack.append(c)
            continue
        if c in close_braces:
            if len(stack) == 0:
                continue
            if stack[-1] == close_braces[close_braces.index(c)]:
                stack.pop()
                continue
            if c == ')' and stack[-1]!= '(':
                continue
            if c == ']' and stack[-1]!= '[':
                continue
            if c == '}' and stack[-1]!= '{':
                continue
    if len(stack)!= 0:
        return []
    else:
        return [paren_string]

