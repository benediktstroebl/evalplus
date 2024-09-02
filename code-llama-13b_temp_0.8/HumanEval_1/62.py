from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    list_of_parentheses_groups = []
    parentheses_group = []
    last_index = 0
    index = 0
    for index, item in enumerate(paren_string):
        if item == "(":
            parentheses_group.append(item)
        elif item == ")":
            parentheses_group.append(item)
            list_of_parentheses_groups.append("".join(parentheses_group))
            parentheses_group = []
            last_index = index
        else:
            continue
    return list_of_parentheses_groups

