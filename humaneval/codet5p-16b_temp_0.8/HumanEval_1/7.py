from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # paren_string = paren_string.replace(" ", "")
    stack = []
    count = 0
    for ch in paren_string:
        if ch == '(':
            stack.append('(')
            count += 1
        else:
            if count == 0:
                continue
            else:
                stack.pop()
                count -= 1
    return [''.join(i) for i in stack]

