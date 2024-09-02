from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.strip()
    brackets = list()
    nested_brackets = list()
    for c in paren_string:
        if c == "(":
            brackets.append(c)
        elif c == ")":
            brackets.pop()
        if brackets:
            nested_brackets.append(brackets[-1])
        if c!= " " and brackets:
            nested_brackets.append(brackets[-1])
    return nested_brackets
