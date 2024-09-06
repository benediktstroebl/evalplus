from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    parentheses = list(paren_string)
    current_group = []
    group_list = []
    for item in parentheses:
        if item == "(":
            current_group.append(item)
        elif item == ")":
            if len(current_group) == 0:
                group_list.append("")
            else:
                current_group.append(item)
                group_list.append("".join(current_group))
                current_group = []
        else:
            current_group.append(item)
    return group_list

