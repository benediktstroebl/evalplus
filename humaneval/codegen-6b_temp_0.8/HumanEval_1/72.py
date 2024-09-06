from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    opening_indices = []
    for i, char in enumerate(paren_string):
        if char == "(":
            opening_indices.append(i)
        elif char == ")":
            if len(opening_indices) == 0:
                return [paren_string[:i + 1]]
            else:
                opening_index = opening_indices.pop()
                paren_string = paren_string[:opening_index + 1] + "_" + paren_string[i + 1:]
    groups = [s.strip() for s in paren_string.split("_") if s]
    return groups

