from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return_list = []
    paren_stack = []
    paren_group_start = 0
    for i, char in enumerate(paren_string):
        if char == "(":
            if not paren_stack:
                paren_group_start = i
            paren_stack.append(char)
        if char == ")":
            paren_stack.pop()
            if not paren_stack:
                return_list.append(paren_string[paren_group_start: i + 1])
    return return_list

