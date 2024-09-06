from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    res = []
    l_count, r_count = 0, 0
    start, end = -1, -1
    for i, c in enumerate(paren_string):
        if c == "(":
            if l_count == 0:
                start = i
            l_count += 1
        elif c == ")":
            r_count += 1
            if l_count == r_count:
                end = i
                res.append(paren_string[start:end + 1])
                l_count, r_count = 0, 0
    return res

