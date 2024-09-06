from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    list_of_separate_groups: List[str] = []
    if len(paren_string) == 0:
        return list_of_separate_groups
    open_paren_stack = []
    open_paren_index = 0
    closed_paren_index = 0
    while closed_paren_index < len(paren_string):
        if paren_string[closed_paren_index] == "(":
            open_paren_stack.append(closed_paren_index)
            closed_paren_index += 1
            continue
        elif len(open_paren_stack) > 0:
            open_paren_index = open_paren_stack.pop()
            list_of_separate_groups.append(
                paren_string[open_paren_index : closed_paren_index + 1]
            )
            closed_paren_index += 1
            continue
        closed_paren_index += 1
    return list_of_separate_groups

