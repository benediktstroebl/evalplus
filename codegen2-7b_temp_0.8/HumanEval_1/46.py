from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    group_start = 0
    separated_groups = []
    group_stack = []

    for index, char in enumerate(paren_string):
        if char == "(":
            group_stack.append(group_start)
            group_start = index + 1
        elif char == ")":
            if not group_stack:
                raise ValueError("Group stack is empty.")
            group_stack.pop()
    separated_groups.append(paren_string[group_start:len(paren_string)])
    return separated_
