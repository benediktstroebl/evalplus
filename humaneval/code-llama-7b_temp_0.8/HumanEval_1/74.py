from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    opening_brace_indices = []
    closing_brace_indices = []
    groups = []

    for i, char in enumerate(paren_string):
        if char == "(":
            opening_brace_indices.append(i)
        elif char == ")":
            closing_brace_indices.append(i)

    # Grouping the indices based on the opening brace index
    for i in range(len(opening_brace_indices)):
        groups.append(
            paren_string[
                opening_brace_indices[i] : closing_brace_indices[i] + 1
            ]
        )

    return groups

