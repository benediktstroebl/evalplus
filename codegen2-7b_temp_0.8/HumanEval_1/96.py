from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    groups: List[str] = []

    curr_group = ""
    for i, char in enumerate(paren_string):
        if char == "(":
            curr_group += char
        elif char == ")":
            curr_group += char

            if not curr_group:
                continue

            groups.append(curr_group)
            curr_group = ""
        elif char == " ":
            continue
        else:
            curr_group += char

    return
