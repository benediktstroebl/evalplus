from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_stack = []  # type: List[str]
    groups = []  # type: List[str]

    for letter in paren_string:
        if letter == "(":
            paren_stack.append(letter)
        elif letter == ")":
            opened_bracket = paren_stack.pop()
            while opened_bracket != "(":
                groups.append(opened_bracket)
                opened_bracket = paren_stack.pop()
        else:
            continue

    while paren_stack:
        groups.append(paren_stack.pop())

    return groups

