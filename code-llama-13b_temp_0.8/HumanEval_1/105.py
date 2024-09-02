from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Hint: use stack to keep track of open parentheses
    if not paren_string or paren_string.strip() == '':
        return []
    paren_stack, result = [], []
    start = -1
    for index, char in enumerate(paren_string):
        if char == '(':
            if not paren_stack:
                start = index
            paren_stack.append(char)
        elif char == ')':
            paren_stack.pop()
            if not paren_stack:
                result.append(paren_string[start:index+1])
    return result

