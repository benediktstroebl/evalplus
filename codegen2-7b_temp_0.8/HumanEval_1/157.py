from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_groups = []
    for group in paren_string.split():
        if group in ["()", "{}", "[]", "{}[]"]:
            continue
        if group == "" or group == " ":
            continue
        if paren_string.count(group) % 2 == 0:
            paren_groups.append(group)
        else:
            paren_groups.append(group.strip('()'))
    return paren_
