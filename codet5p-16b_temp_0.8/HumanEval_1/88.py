from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    open_parens = []
    stack = []
    for index, c in enumerate(paren_string):
        if c == '(':
            open_parens.append(index)
            stack.append(c)
        elif c == ')':
            if len(stack) > 0 and stack[-1] == '(':
                open_parens.pop()
                stack.pop()
            else:
                stack.append(c)
    print(open_parens)
    print(stack)
    result = []
    for index in open_parens:
        result.append(paren_string[0:index])
        result.append(paren_string[index:])
    return result

