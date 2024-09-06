from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    new_string = ""
    lst = []
    level = 0
    for i in paren_string:
        if i == "(":
            level += 1
        elif i == ")":
            level -= 1
        if level == 0:
            lst.append(new_string)
            new_string = ""
        else:
            new_string += i
    return lst

