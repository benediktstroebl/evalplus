from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = []
    paren_index = 0
    paren_groups = []

    for index, char in enumerate(paren_string):
        if char == "(":
            stack.append(index)
        if char == ")":
            stack.pop()
            if not stack:
                paren_index = index

    paren_groups.append(paren_string[:paren_index + 1])
    paren_groups.append(paren_string[paren_index + 2:])

    return paren_groups

