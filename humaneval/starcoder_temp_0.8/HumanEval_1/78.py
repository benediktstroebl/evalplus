from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    groups = []
    buffer = []
    for c in paren_string:
        if c == "(":
            buffer.append(c)
        elif c == ")":
            if len(buffer) == 0:
                raise ValueError("Ill-formed parentheses")
            buffer.pop()
            if len(buffer) == 0:
                groups.append("".join(paren_string[len(groups) * 2 :]))

    if len(buffer) > 0:
        raise ValueError("Ill-formed parentheses")

    return groups

