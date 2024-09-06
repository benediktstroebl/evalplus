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
    paren_stack = []

    for i, char in enumerate(paren_string):
        if char == '(':
            paren_stack.append(i)
        elif char == ')':
            if not paren_stack:
                return []
            start_index = paren_stack.pop()
            result.append(paren_string[start_index: i + 1])

    if paren_stack:
        return []

    return result

