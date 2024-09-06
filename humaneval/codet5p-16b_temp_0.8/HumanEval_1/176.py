from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    paren_list = list(paren_string)
    sep_list = []
    curr_str = ""
    while paren_list:
        c = paren_list.pop(0)
        if c == " ":
            continue
        if c == "(":
            if curr_str:
                sep_list.append(curr_str)
                curr_str = ""
            curr_str += c
        elif c == ")":
            curr_str += c
            if curr_str:
                sep_list.append(curr_str)
                curr_str = ""
        else:
            curr_str += c
    sep_list.append(curr_str)
    return sep_list

