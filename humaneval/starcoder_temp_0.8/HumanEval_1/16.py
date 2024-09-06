from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # (GroupStart, GroupEnd)
    pairs = {'(': ')', '[': ']', '{': '}'}
    stack = []
    result = []
    for c in paren_string:
        if c in pairs:
            stack.append(c)
        elif len(stack) == 0:
            return []
        else:
            if c == pairs[stack[-1]]:
                stack.pop()
            else:
                return []

    for item in stack[::-1]:
        result.append(pairs[item] * 2)
    return result

