from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    open_list = []
    result = []
    for char in paren_string:
        if char == "(":
            open_list.append(char)
        elif char == ")":
            if len(open_list) > 0:
                open_list.pop(-1)
            else:
                result.append(char)
        elif char == " ":
            continue
        else:
            result.append(char)
    if len(open_list) == 0:
        return result
    else:
        raise SyntaxError("There is a parenthesis mismatch")

