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
    curr_str = ""
    paren_count = 0
    for char in paren_string:
        if char == "(":
            if paren_count > 0:
                curr_str += char
            paren_count += 1
        elif char == ")":
            if paren_count > 1:
                curr_str += char
            paren_count -= 1
        else:
            curr_str += char

        if paren_count == 0:
            ret_list.append(curr_str)
            curr_str = ""

    return ret_list

