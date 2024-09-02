from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if paren_string is None or paren_string == "":
        return []

    paren_groups = []
    paren_stack = []
    for i, character in enumerate(paren_string):
        if character == "(":
            if i!= 0 and paren_string[i-1] == " ":
                continue
            paren_stack.append(character)
        elif character == ")":
            if i!= 0 and paren_string[i-1] == " ":
                continue
            paren_stack.append(character)
            if len(paren_stack) > 1:
                paren_groups.append(paren_stack[1:-1])
            paren_stack = []
        else:
            continue

    return paren_groups

