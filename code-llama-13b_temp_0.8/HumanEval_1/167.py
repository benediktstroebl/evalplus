from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Solution 1
    res = []
    start = 0
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            if not res:
                res.append(paren_string[start : i + 1])
            else:
                res[-1] += paren_string[i]
        elif paren_string[i] == ')' and res:
            res[-1] += paren_string[i]
            if not paren_balanced(res[-1]):
                start = i + 1
    return res

