from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    ret_list = []
    group = []
    level = 0
    for i in paren_string:
        if i == "(":
            level += 1
        elif i == ")":
            level -= 1
        if level == 0:
            ret_list.append("".join(group))
            group = []
        else:
            group.append(i)
    return ret_list

