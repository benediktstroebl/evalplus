from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # this is really an interesting problem for you to look into
    # I can convert this into a stack approach
    # so I can remove the outmost open parentheses
    paren_stack = []
    idx = 0
    result = []
    while idx < len(paren_string):
        if paren_string[idx] == '(':
            paren_stack.append(paren_string[idx])
        elif paren_string[idx] == ')':
            paren_stack.pop()
            if len(paren_stack) == 0:
                result += [paren_string[:idx + 1], paren_string[idx + 1:]]
                idx = idx + 1
        idx += 1
    return result

