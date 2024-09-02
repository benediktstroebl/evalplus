from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    balanced_group_list = []
    paren_group = ""
    paren_counter = 0

    for char in paren_string:
        if char == "(":
            paren_counter += 1
        elif char == ")":
            paren_counter -= 1

        paren_group += char

        if paren_counter == 0:
            balanced_group_list.append(paren_group.strip())
            paren_group = ""

    return balanced_group_list

