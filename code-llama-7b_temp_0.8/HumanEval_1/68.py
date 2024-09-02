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
    paren_group_list = []
    for index, character in enumerate(paren_string):
        if character == "(":
            paren_stack.append(index)
        elif character == ")":
            paren_stack.pop()
            if not paren_stack:
                paren_group_list.append(paren_string[paren_stack[0] : index + 1])
                paren_stack = []

    for group in paren_group_list:
        group = group.replace(" ", "")
        return_list.append(group)

    return return_list

