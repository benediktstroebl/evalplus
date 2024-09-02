from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_list = []
    start_index = 0
    while start_index < len(paren_string):
        open_parens = 0
        for i, ch in enumerate(paren_string[start_index:]):
            if ch == "(":
                open_parens += 1
            elif ch == ")":
                open_parens -= 1
            if open_parens == 0:
                paren_list.append(paren_string[start_index : start_index + i + 1])
                start_index += i + 1
                break
    return paren_
