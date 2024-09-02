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
    next_group = []
    stack = [[]]
    for s in paren_string:
        if s == ')':
            if len(stack[-1]) == 0:
                stack.pop()
                result.append("".join(next_group))
                stack.append(next_group)
                next_group = []
                continue

            stack[-1].append(s)
            next_group.append(s)
        elif s == '(':
            stack.append([])
        elif s == ' ':
            next_group.append(s)
        else:
            stack[-1].append(s)
            next_group.append(s)
    result.append("".join(stack[-1]))

    return result

