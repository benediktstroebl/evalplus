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
    curr_group = []
    for index, character in enumerate(paren_string):
        if character == '(':
            stack.append(index)
            curr_group.append(index)
        elif character == ')':
            curr_group.append(index)
            stack.pop()
    paren_groups = []
    for index in curr_group:
        left_index = max(stack)
        left_open_paren = paren_string[left_index]
        right_index = min(curr_group)
        right_close_paren = paren_string[right_index]
        if left_open_paren == '(' and right_close_paren == ')':
            paren_groups.append(paren_string[left_index:right_index + 1])
    return paren_groups

