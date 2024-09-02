from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if len(paren_string) == 2 and paren_string[0] == "(" and paren_string[1] == ")":
        return ["()"]
    elif len(paren_string) == 0:
        return []
    elif paren_string[0] == "(":
        return separate_paren_groups(paren_string[1:])
    elif paren_string[0] != "(" and paren_string[0] != ")":
        return separate_paren_groups(paren_string[1:]) + separate_paren_groups(paren_string[0:1])
    elif paren_string[0] == ")" and len(paren_string) > 1:
        return separate_paren_groups(paren_string[1:]) + ["()"]
    elif paren_string[0] == ")":
        return ["()"]

