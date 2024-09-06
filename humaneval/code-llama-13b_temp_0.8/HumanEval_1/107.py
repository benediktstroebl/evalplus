from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # HINT: you don't need to use regexp for this task!
    result = []
    current = ''
    level = 0
    for c in paren_string:
        if c == '(':
            level += 1
        if c == ')':
            level -= 1
        if c in '()':
            current += c
        if level == 0 and current:
            result.append(current)
            current = ''
    return result

