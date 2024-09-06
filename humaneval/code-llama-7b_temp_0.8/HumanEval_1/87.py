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
    splited_list = []
    for i in paren_string:
        if i == "(":
            stack.append(i)
        elif i == ")":
            stack.pop()
        elif i != " ":
            splited_list.append(i)
    return splited_list

