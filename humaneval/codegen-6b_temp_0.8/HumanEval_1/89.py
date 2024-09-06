from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # visited = []
    # for i in range(len(paren_string)):
    #     if paren_string[i] == ')':
    #         if visited:
    #             visited.pop()
    #         else:
    #             return []
    #     else:
    #         visited.append(paren_string[i])
    # return visited
    stack = []
    for i in paren_string:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if stack:
                stack.pop()
            else:
                return []
    return stack

