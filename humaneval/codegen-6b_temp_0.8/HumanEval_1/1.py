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
    stack = []

    for i in range(len(paren_string)):
        c = paren_string[i]
        if c == '(':
            stack.append(i)
        elif c == ')':
            start = stack.pop()
            substr = paren_string[start:i + 1]
            while stack:
                paren_index = stack.pop()
                substr = paren_string[paren_index: i + 1]
            result.append(substr)

    return result

