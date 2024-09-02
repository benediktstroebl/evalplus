from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    current_depth = 0
    current_start = 0
    all_groups = []
    for i, paren in enumerate(paren_string):
        if paren == "(":
            if current_depth == 0:
                current_start = i
            current_depth += 1
        elif paren == ")":
            current_depth -= 1
            if current_depth == 0:
                all_groups.append(paren_string[current_start:i+1])

    return all_groups

