from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_count = 0
    groups = []
    for paren_string in paren_string.split(" "):
        if paren_string == "":
            groups.append("")
        else:
            groups.append(paren_string)
            paren_count += 1
            if paren_count == len(paren_string):
                groups[-1] = groups[-1].lstrip(" ()")
    return groups

